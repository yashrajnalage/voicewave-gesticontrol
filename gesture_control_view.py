
import cv2
import numpy as np
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                             QHBoxLayout, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QColor
from base_view import BaseView

class HandGestureVisualizer(QWidget):
    """Custom widget for hand gesture visualization"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(300)
        self.is_detecting = False
        self.corner_opacity = [0.3, 0.5, 0.7, 0.9]
        self.scan_position = 0
        self.scan_timer = QTimer()
        self.scan_timer.timeout.connect(self.update_scan)
        
    def setDetecting(self, detecting):
        """Set detecting state and update visualization"""
        self.is_detecting = detecting
        if detecting:
            self.scan_timer.start(50)
        else:
            self.scan_timer.stop()
        self.update()
        
    def update_scan(self):
        """Update scanning animation"""
        self.scan_position = (self.scan_position + 1) % 100
        
        # Pulse the corner opacity
        for i in range(4):
            self.corner_opacity[i] = 0.3 + 0.6 * abs(np.sin((self.scan_position + i * 25) / 50 * np.pi))
        
        self.update()
        
    def paintEvent(self, event):
        """Draw the camera feed placeholder and detection visualization"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw background
        painter.fillRect(self.rect(), QColor(0, 0, 0, 180))
        
        if not self.is_detecting:
            # Draw inactive state text
            painter.setPen(QColor(150, 150, 150))
            painter.drawText(self.rect(), Qt.AlignCenter, "Camera feed not active")
            return
        
        # Draw active scanning text
        painter.setPen(QColor(139, 92, 246))
        painter.drawText(self.rect(), Qt.AlignCenter, "Scanning for hand gestures...")
        
        # Draw scanning line
        scan_y = int(self.height() * (self.scan_position / 100))
        gradient_pen = QPen(QColor(139, 92, 246, 150), 2)
        painter.setPen(gradient_pen)
        painter.drawLine(0, scan_y, self.width(), scan_y)
        
        # Draw corner markers
        corner_size = 20
        corners = [
            (0, 0, corner_size, corner_size, 0, 0),  # Top-left
            (self.width() - corner_size, 0, corner_size, corner_size, 1, 0),  # Top-right
            (0, self.height() - corner_size, corner_size, corner_size, 0, 1),  # Bottom-left
            (self.width() - corner_size, self.height() - corner_size, corner_size, corner_size, 1, 1)  # Bottom-right
        ]
        
        for i, (x, y, w, h, h_dir, v_dir) in enumerate(corners):
            painter.setPen(QPen(QColor(139, 92, 246, int(255 * self.corner_opacity[i])), 2))
            
            # Draw L-shaped corners
            if h_dir == 0:  # Left side
                painter.drawLine(x, y, x + corner_size//2, y)
                painter.drawLine(x, y, x, y + corner_size//2)
            else:  # Right side
                painter.drawLine(x + corner_size, y, x + corner_size//2, y)
                painter.drawLine(x + corner_size, y, x + corner_size, y + corner_size//2)
                
            if v_dir == 0:  # Top side
                if h_dir == 1:
                    painter.drawLine(x + corner_size, y, x + corner_size, y + corner_size//2)
            else:  # Bottom side
                if h_dir == 0:
                    painter.drawLine(x, y + corner_size, x, y + corner_size//2)
                    painter.drawLine(x, y + corner_size, x + corner_size//2, y + corner_size)
                else:
                    painter.drawLine(x + corner_size, y + corner_size, x + corner_size//2, y + corner_size)
                    painter.drawLine(x + corner_size, y + corner_size, x + corner_size, y + corner_size//2)


class GestureControlView(BaseView):
    """View for the gesture control functionality"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_detecting = False
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.update_camera_feed)
        self.cap = None
        
    def setup_ui(self):
        """Set up the UI components"""
        super().setup_ui()
        
        # Main title
        title_label = QLabel("Gesture Control")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Control your system using hand gestures")
        subtitle_label.setStyleSheet("font-size: 14px; color: #888;")
        self.main_layout.addWidget(subtitle_label)
        
        # Main content layout
        content_layout = QHBoxLayout()
        
        # Left column - Camera feed and controls
        left_layout = QVBoxLayout()
        
        # Camera view
        self.gesture_visualizer = HandGestureVisualizer()
        self.gesture_visualizer.setStyleSheet("background-color: #222; border-radius: 10px;")
        left_layout.addWidget(self.gesture_visualizer)
        
        # Status indicator
        status_layout = QHBoxLayout()
        status_label = QLabel("Status:")
        self.status_indicator = QLabel("Inactive")
        self.status_indicator.setStyleSheet("color: #888; font-weight: bold;")
        status_layout.addWidget(status_label)
        status_layout.addWidget(self.status_indicator)
        status_layout.addStretch()
        left_layout.addLayout(status_layout)
        
        # Start/Stop button
        button_layout = QHBoxLayout()
        self.toggle_button = QPushButton("Start Camera")
        self.toggle_button.setMinimumHeight(40)
        self.toggle_button.clicked.connect(self.toggle_detection)
        button_layout.addStretch()
        button_layout.addWidget(self.toggle_button)
        button_layout.addStretch()
        left_layout.addLayout(button_layout)
        
        # Tips box
        tips_box = QWidget()
        tips_layout = QVBoxLayout(tips_box)
        tips_title = QLabel("Gesture Control Tips")
        tips_title.setStyleSheet("font-weight: bold;")
        tips_text = QLabel("Try gestures like swiping left/right to navigate, pinch to zoom, "
                          "or raising your hand with an open palm to pause/resume.")
        tips_text.setWordWrap(True)
        tips_layout.addWidget(tips_title)
        tips_layout.addWidget(tips_text)
        tips_box.setStyleSheet("background-color: rgba(139, 92, 246, 0.2); border-radius: 5px; padding: 10px;")
        left_layout.addWidget(tips_box)
        
        # Right column - Command history
        right_layout = QVBoxLayout()
        history_title = QLabel("Command History")
        history_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        right_layout.addWidget(history_title)
        
        self.command_list = QListWidget()
        self.command_list.setAlternatingRowColors(True)
        self.command_list.setStyleSheet("alternate-background-color: #2A2F3C;")
        right_layout.addWidget(self.command_list)
        
        # Add demo commands
        self.add_demo_commands()
        
        # Add layouts to main content
        content_layout.addLayout(left_layout, 2)
        content_layout.addLayout(right_layout, 1)
        
        self.main_layout.addLayout(content_layout)
        self.main_layout.addLayout(self.nav_layout)

    def add_demo_commands(self):
        """Add demo commands to the command history"""
        commands = [
            {"command": "Swipe Left", "timestamp": "10:20 AM", "status": "success"},
            {"command": "Pinch Zoom", "timestamp": "10:18 AM", "status": "success"},
            {"command": "Scroll Down", "timestamp": "10:15 AM", "status": "error"},
            {"command": "Click", "timestamp": "10:14 AM", "status": "success"},
        ]
        
        for cmd in commands:
            item = QListWidgetItem(f"{cmd['timestamp']} - {cmd['command']}")
            if cmd["status"] == "success":
                item.setForeground(QColor(0, 200, 0))
            else:
                item.setForeground(QColor(255, 0, 0))
            self.command_list.addItem(item)

    def toggle_detection(self):
        """Toggle gesture detection on/off"""
        self.is_detecting = not self.is_detecting
        
        if self.is_detecting:
            # Start detection
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.gesture_visualizer.setDetecting(False)
                return
                
            self.toggle_button.setText("Stop Camera")
            self.status_indicator.setText("Active")
            self.status_indicator.setStyleSheet("color: #8B5CF6; font-weight: bold;")
            self.gesture_visualizer.setDetecting(True)
            self.camera_timer.start(30)
        else:
            # Stop detection
            self.camera_timer.stop()
            if self.cap:
                self.cap.release()
                self.cap = None
            self.is_detecting = False
            self.toggle_button.setText("Start Camera")
            self.status_indicator.setText("Inactive")
            self.status_indicator.setStyleSheet("color: #888; font-weight: bold;")
            self.gesture_visualizer.setDetecting(False)

    def update_camera_feed(self):
        """Update the camera feed with gesture detection visualization"""
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                # Here you would add actual hand gesture detection
                # For now, we just update the visualizer
                pass

    def closeEvent(self, event):
        """Handle close event to release the camera"""
        if self.cap:
            self.cap.release()
        super().closeEvent(event)
