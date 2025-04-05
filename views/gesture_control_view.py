
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                           QGridLayout, QFrame, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor
from views.base_view import BaseView
import random
import math

class HandGestureVisualizer(QFrame):
    """Visualizer for hand gestures"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_detecting = False
        self.setMinimumHeight(200)
        self.setup_ui()
        self.scan_pos = 0
        
    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #1A1F2C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
        """)
        
        self.layout = QVBoxLayout()
        
        # Status text
        self.status_label = QLabel("Camera feed not active")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #B0B0B0;")
        
        self.layout.addWidget(self.status_label)
        self.setLayout(self.layout)
        
    def set_detecting(self, detecting):
        """Set the detection state and update UI"""
        self.is_detecting = detecting
        
        if detecting:
            self.status_label.setText("Scanning for hand gestures...")
            self.status_label.setStyleSheet("color: #10B981;")
            
            # Start the scanning animation
            self.scan_timer = QTimer(self)
            self.scan_timer.timeout.connect(self.update_scan_line)
            self.scan_timer.start(50)
        else:
            self.status_label.setText("Camera feed not active")
            self.status_label.setStyleSheet("color: #B0B0B0;")
            
            if hasattr(self, 'scan_timer'):
                self.scan_timer.stop()
                
    def update_scan_line(self):
        """Update the scan line position for animation"""
        self.scan_pos += 5
        if self.scan_pos > self.height():
            self.scan_pos = 0
        self.update()
        
    def paintEvent(self, event):
        """Custom paint event to draw scan line and corner brackets"""
        super().paintEvent(event)
        
        if not self.is_detecting:
            return
            
        from PyQt5.QtGui import QPainter, QPen
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw scan line
        pen = QPen(QColor(16, 185, 129), 2)
        painter.setPen(pen)
        painter.drawLine(0, self.scan_pos, self.width(), self.scan_pos)
        
        # Draw corner brackets
        pen = QPen(QColor(139, 92, 246), 2)
        painter.setPen(pen)
        
        # Top-left corner
        painter.drawLine(0, 0, 20, 0)
        painter.drawLine(0, 0, 0, 20)
        
        # Top-right corner
        painter.drawLine(self.width()-20, 0, self.width(), 0)
        painter.drawLine(self.width(), 0, self.width(), 20)
        
        # Bottom-left corner
        painter.drawLine(0, self.height(), 0, self.height()-20)
        painter.drawLine(0, self.height(), 20, self.height())
        
        # Bottom-right corner
        painter.drawLine(self.width(), self.height(), self.width(), self.height()-20)
        painter.drawLine(self.width(), self.height(), self.width()-20, self.height())


class GestureControlView(BaseView):
    """Gesture control view for the application"""
    
    def __init__(self, parent=None):
        self.is_detecting = False
        self.commands = [
            {"id": "1", "type": "gesture", "command": "Swipe Left", "timestamp": "10:20 AM", "status": "success"},
            {"id": "2", "type": "gesture", "command": "Pinch Zoom", "timestamp": "10:18 AM", "status": "success"},
            {"id": "3", "type": "gesture", "command": "Scroll Down", "timestamp": "10:15 AM", "status": "error"},
            {"id": "4", "type": "gesture", "command": "Click", "timestamp": "10:14 AM", "status": "success"},
        ]
        super().__init__(parent)
        
    def setup_ui(self):
        super().setup_ui()
        
        # Title
        title_label = QLabel("Gesture Control")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.main_layout.addWidget(title_label)
        
        subtitle = QLabel("Control your system using hand gestures")
        subtitle.setStyleSheet("color: #B0B0B0;")
        self.main_layout.addWidget(subtitle)
        
        # Main content layout (grid with gesture control and history)
        content_layout = QGridLayout()
        
        # Gesture control card
        gesture_control = QFrame()
        gesture_control.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
        """)
        
        gc_layout = QVBoxLayout(gesture_control)
        
        # Header with title and status
        header_layout = QHBoxLayout()
        gc_title = QLabel("Hand Gesture Recognition")
        gc_title.setFont(QFont("Arial", 14, QFont.Bold))
        
        self.status_label = QLabel("Inactive")
        self.status_label.setStyleSheet("""
            background-color: transparent;
            color: #B0B0B0;
            border: 1px solid #B0B0B0;
            border-radius: 10px;
            padding: 2px 8px;
        """)
        
        header_layout.addWidget(gc_title)
        header_layout.addStretch()
        header_layout.addWidget(self.status_label)
        
        gc_layout.addLayout(header_layout)
        
        # Hand gesture visualizer
        self.visualizer = HandGestureVisualizer()
        gc_layout.addWidget(self.visualizer)
        
        # Camera toggle button
        button_layout = QHBoxLayout()
        self.camera_button = QPushButton()
        self.camera_button.setStyleSheet("""
            QPushButton {
                background-color: #6D28D9;
                border-radius: 5px;
                color: white;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #5B21B6;
            }
        """)
        self.camera_button.setText("📷 Start Camera")
        self.camera_button.clicked.connect(self.toggle_detection)
        
        button_layout.addStretch()
        button_layout.addWidget(self.camera_button)
        button_layout.addStretch()
        
        gc_layout.addLayout(button_layout)
        
        # Tips section
        tips_frame = QFrame()
        tips_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(139, 92, 246, 0.1);
                border-radius: 5px;
            }
        """)
        
        tips_layout = QHBoxLayout(tips_frame)
        
        tips_icon = QLabel("ℹ️")
        
        tips_content = QVBoxLayout()
        tips_title = QLabel("Gesture Control Tips")
        tips_title.setFont(QFont("Arial", 10, QFont.Bold))
        
        tips_text = QLabel("Try gestures like swiping left/right to navigate, pinch to zoom, or raising your hand with an open palm to pause/resume.")
        tips_text.setWordWrap(True)
        tips_text.setStyleSheet("color: #B0B0B0;")
        
        tips_content.addWidget(tips_title)
        tips_content.addWidget(tips_text)
        
        tips_layout.addWidget(tips_icon)
        tips_layout.addLayout(tips_content)
        
        gc_layout.addWidget(tips_frame)
        
        # Add gesture control to content layout
        content_layout.addWidget(gesture_control, 0, 0, 1, 2)
        
        # Command history
        from views.voice_command_view import CommandHistory
        history_widget = CommandHistory(self.commands)
        content_layout.addWidget(history_widget, 0, 2)
        
        content_layout.setColumnStretch(0, 2)
        content_layout.setColumnStretch(2, 1)
        
        self.main_layout.addLayout(content_layout)
        
    def toggle_detection(self):
        """Toggle the gesture detection state"""
        self.is_detecting = not self.is_detecting
        
        if self.is_detecting:
            self.camera_button.setText("📷 Stop Camera")
            self.camera_button.setStyleSheet("""
                QPushButton {
                    background-color: #EF4444;
                    border-radius: 5px;
                    color: white;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #DC2626;
                }
            """)
            self.status_label.setText("Active")
            self.status_label.setStyleSheet("""
                background-color: #8B5CF6;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 2px 8px;
            """)
            
            # Activate the visualizer
            self.visualizer.set_detecting(True)
        else:
            self.camera_button.setText("📷 Start Camera")
            self.camera_button.setStyleSheet("""
                QPushButton {
                    background-color: #6D28D9;
                    border-radius: 5px;
                    color: white;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #5B21B6;
                }
            """)
            self.status_label.setText("Inactive")
            self.status_label.setStyleSheet("""
                background-color: transparent;
                color: #B0B0B0;
                border: 1px solid #B0B0B0;
                border-radius: 10px;
                padding: 2px 8px;
            """)
            
            # Deactivate the visualizer
            self.visualizer.set_detecting(False)
