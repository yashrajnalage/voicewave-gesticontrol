
import numpy as np
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                             QHBoxLayout, QListWidget, QListWidgetItem, QFrame)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPen
from base_view import BaseView

class VoiceVisualizer(QWidget):
    """Custom widget for voice visualization"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(80)
        self.levels = [5] * 12
        self.active = False
        
    def setActive(self, active):
        """Set active state and update visualization"""
        self.active = active
        self.update()
        
    def setLevels(self, levels):
        """Update audio level data"""
        self.levels = levels
        self.update()
        
    def paintEvent(self, event):
        """Draw the audio visualizer"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        width = self.width()
        height = self.height()
        
        # Calculate bar width and spacing
        num_bars = len(self.levels)
        bar_width = (width - (num_bars - 1) * 2) / num_bars
        
        # Draw the visualization bars
        for i, level in enumerate(self.levels):
            # Map level to height
            bar_height = (level / 100) * height
            
            # Set color based on active state
            if self.active:
                color = QColor(139, 92, 246)  # Purple for active
            else:
                color = QColor(100, 100, 100)  # Gray for inactive
            
            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
            
            x = i * (bar_width + 2)
            y = height - bar_height
            
            painter.drawRoundedRect(int(x), int(y), int(bar_width), int(bar_height), 2, 2)


class VoiceCommandView(BaseView):
    """View for the voice command functionality"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_listening = False
        self.visualizer_timer = QTimer()
        self.visualizer_timer.timeout.connect(self.update_visualizer)
        self.visualizer_levels = []
        
    def setup_ui(self):
        """Set up the UI components"""
        super().setup_ui()
        
        # Main title
        title_label = QLabel("Voice Command Control")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Control your system using voice commands")
        subtitle_label.setStyleSheet("font-size: 14px; color: #888;")
        self.main_layout.addWidget(subtitle_label)
        
        # Main content layout
        content_layout = QHBoxLayout()
        
        # Left column - Voice visualization and controls
        left_layout = QVBoxLayout()
        
        # Microphone button and visualizer
        mic_container = QWidget()
        mic_container.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 20px;")
        mic_layout = QVBoxLayout(mic_container)
        
        # Status indicator
        status_layout = QHBoxLayout()
        status_label = QLabel("Status:")
        self.status_indicator = QLabel("Idle")
        self.status_indicator.setStyleSheet("color: #888; font-weight: bold;")
        status_layout.addWidget(status_label)
        status_layout.addWidget(self.status_indicator)
        status_layout.addStretch()
        mic_layout.addLayout(status_layout)
        
        # Visualizer
        self.visualizer = VoiceVisualizer()
        self.visualizer.setStyleSheet("background-color: #1E212A; border-radius: 5px;")
        mic_layout.addWidget(self.visualizer)
        
        # Recognized text display
        text_layout = QVBoxLayout()
        text_label = QLabel("Recognized Text:")
        self.text_display = QLabel("Click the microphone to start")
        self.text_display.setStyleSheet("background-color: #1E212A; border-radius: 5px; padding: 10px; min-height: 40px;")
        text_layout.addWidget(text_label)
        text_layout.addWidget(self.text_display)
        mic_layout.addLayout(text_layout)
        
        # Microphone button
        button_layout = QHBoxLayout()
        self.toggle_button = QPushButton("Start Listening")
        self.toggle_button.setMinimumHeight(40)
        self.toggle_button.clicked.connect(self.toggle_listening)
        button_layout.addStretch()
        button_layout.addWidget(self.toggle_button)
        button_layout.addStretch()
        mic_layout.addLayout(button_layout)
        
        left_layout.addWidget(mic_container)
        
        # Tips box
        tips_box = QWidget()
        tips_layout = QVBoxLayout(tips_box)
        tips_title = QLabel("Voice Command Tips")
        tips_title.setStyleSheet("font-weight: bold;")
        tips_text = QLabel("Try commands like \"Open Browser\", \"Volume Up\", \"Close Window\", or \"Scroll Down\" to control your system.")
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
        
        # Add navigation bar at the bottom
        self.main_layout.addLayout(self.nav_layout)
        
    def add_demo_commands(self):
        """Add demo commands to the command history"""
        commands = [
            {"command": "Open Browser", "timestamp": "10:15 AM", "status": "success"},
            {"command": "Volume Up", "timestamp": "10:12 AM", "status": "success"},
            {"command": "Launch Spotify", "timestamp": "10:10 AM", "status": "error"},
            {"command": "Next Slide", "timestamp": "10:05 AM", "status": "success"},
        ]
        
        for cmd in commands:
            item = QListWidgetItem(f"{cmd['timestamp']} - {cmd['command']}")
            if cmd["status"] == "success":
                item.setForeground(QColor(0, 200, 0))
            else:
                item.setForeground(QColor(255, 0, 0))
            self.command_list.addItem(item)

    def toggle_listening(self):
        """Toggle voice recognition on/off"""
        self.is_listening = not self.is_listening
        
        if self.is_listening:
            # Start listening
            self.toggle_button.setText("Stop Listening")
            self.status_indicator.setText("Listening")
            self.status_indicator.setStyleSheet("color: #8B5CF6; font-weight: bold;")
            self.text_display.setText("Listening...")
            self.visualizer.setActive(True)
            self.visualizer_timer.start(50)
        else:
            # Stop listening
            self.toggle_button.setText("Start Listening")
            self.status_indicator.setText("Idle")
            self.status_indicator.setStyleSheet("color: #888; font-weight: bold;")
            self.text_display.setText("Click the microphone to start")
            self.visualizer.setActive(False)
            self.visualizer_timer.stop()
    
    def update_visualizer(self):
        """Update the audio visualizer display"""
        if self.is_listening:
            # Generate random visualizer levels for demo
            levels = np.random.randint(10, 70, 12).tolist()
            self.visualizer.setLevels(levels)
