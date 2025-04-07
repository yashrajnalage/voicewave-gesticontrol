
import cv2
import numpy as np
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                             QHBoxLayout, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from views.base_view import BaseView

class GestureControlView(BaseView):
    """View for the gesture control functionality"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
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
        self.camera_label = QLabel()
        self.camera_label.setMinimumSize(400, 300)
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setStyleSheet("background-color: #222; border-radius: 10px;")
        self.camera_label.setText("Camera feed will appear here")
        left_layout.addWidget(self.camera_label)
        
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
                item.setForeground(Qt.green)
            else:
                item.setForeground(Qt.red)
            self.command_list.addItem(item)

    def toggle_detection(self):
        """Toggle gesture detection on/off"""
        if not self.is_detecting:
            # Start detection
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.camera_label.setText("Error: Could not open camera")
                return
                
            self.is_detecting = True
            self.toggle_button.setText("Stop Camera")
            self.status_indicator.setText("Active")
            self.status_indicator.setStyleSheet("color: #8B5CF6; font-weight: bold;")
            self.camera_timer.start(30)  # update every 30ms
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
            self.camera_label.setText("Camera feed will appear here")

    def update_camera_feed(self):
        """Update the camera feed with gesture detection visualization"""
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                # Convert to RGB for display (OpenCV uses BGR)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Here you would add the actual hand gesture detection
                # For now, we'll just add a placeholder rectangle
                cv2.rectangle(frame, (100, 100), (300, 300), (139, 92, 246), 2)
                
                # Convert the image to Qt format
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qt_image)
                self.camera_label.setPixmap(pixmap)

    def closeEvent(self, event):
        """Handle close event to release the camera"""
        if self.cap:
            self.cap.release()
        super().closeEvent(event)
