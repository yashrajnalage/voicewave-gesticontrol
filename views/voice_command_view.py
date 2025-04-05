from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                           QGridLayout, QFrame, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QColor
from views.base_view import BaseView
import random
import math

class VoiceVisualizer(QFrame):
    """Visualizer for voice activity"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(100)
        self.setMinimumWidth(200)
        self.is_active = False
        self.bars = []
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
        """)
        
        # Create layout
        layout = QHBoxLayout()
        layout.setSpacing(5)
        
        # Create bars
        for i in range(12):
            bar = QFrame()
            bar.setFixedWidth(10)
            bar.setFixedHeight(5)  # Default height when inactive
            bar.setStyleSheet("background-color: rgba(139, 92, 246, 0.6); border-radius: 2px;")
            layout.addWidget(bar)
            self.bars.append(bar)
            
        layout.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.setLayout(layout)
        
    def set_active(self, active):
        """Set the visualizer active state and start/stop the animation"""
        self.is_active = active
        if active:
            self.start_animation()
        else:
            self.stop_animation()
            
    def start_animation(self):
        """Start the bar animation"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_bars)
        self.timer.start(100)
        
    def stop_animation(self):
        """Stop the bar animation"""
        if hasattr(self, 'timer'):
            self.timer.stop()
        # Reset all bars to minimum height
        for bar in self.bars:
            bar.setFixedHeight(5)
            
    def update_bars(self):
        """Update the height of each bar"""
        if not self.is_active:
            return
            
        for i, bar in enumerate(self.bars):
            # Calculate height based on a sine wave pattern
            height = int(30 * abs(math.sin((i / 11) * math.pi + random.random()))) + 5
            bar.setFixedHeight(height)


class CommandItem(QFrame):
    """Individual command item for the command history"""
    
    def __init__(self, command_type, command, timestamp, status, parent=None):
        super().__init__(parent)
        self.command_type = command_type
        self.command = command
        self.timestamp = timestamp
        self.status = status
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(139, 92, 246, 0.1);
                border-radius: 5px;
                padding: 5px;
                margin: 2px;
            }
            QLabel {
                color: white;
            }
        """)
        
        layout = QHBoxLayout()
        
        # Icon
        icon = QLabel("🎤" if self.command_type == "voice" else "👋")
        layout.addWidget(icon)
        
        # Command info
        info_layout = QVBoxLayout()
        command_label = QLabel(self.command)
        command_label.setFont(QFont("Arial", 10, QFont.Bold))
        
        time_label = QLabel(self.timestamp)
        time_label.setStyleSheet("color: #B0B0B0; font-size: 8pt;")
        
        info_layout.addWidget(command_label)
        info_layout.addWidget(time_label)
        
        layout.addLayout(info_layout)
        layout.addStretch()
        
        # Status
        status_label = QLabel(self.status)
        if self.status == "success":
            status_label.setStyleSheet("color: #10B981; font-weight: bold;")
        else:
            status_label.setStyleSheet("color: #EF4444; font-weight: bold;")
        layout.addWidget(status_label)
        
        self.setLayout(layout)


class CommandHistory(QFrame):
    """Widget to display command history"""
    
    def __init__(self, commands, parent=None):
        super().__init__(parent)
        self.commands = commands
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
            QLabel {
                color: white;
            }
            QListWidget {
                background-color: transparent;
                border: none;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Title
        title_layout = QHBoxLayout()
        icon = QLabel("⏱️")
        title = QLabel("Command History")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        
        title_layout.addWidget(icon)
        title_layout.addWidget(title)
        title_layout.addStretch()
        
        layout.addLayout(title_layout)
        
        # Command list
        command_list = QVBoxLayout()
        for cmd in self.commands:
            item = CommandItem(cmd["type"], cmd["command"], cmd["timestamp"], cmd["status"])
            command_list.addWidget(item)
            
        layout.addLayout(command_list)
        self.setLayout(layout)


class VoiceCommandView(BaseView):
    """Voice command view for the application"""
    
    def __init__(self, parent=None):
        self.is_listening = False
        self.recognized_text = ""
        self.commands = [
            {"id": "1", "type": "voice", "command": "Open Browser", "timestamp": "10:15 AM", "status": "success"},
            {"id": "2", "type": "voice", "command": "Volume Up", "timestamp": "10:12 AM", "status": "success"},
            {"id": "3", "type": "voice", "command": "Launch Spotify", "timestamp": "10:10 AM", "status": "error"},
            {"id": "4", "type": "voice", "command": "Next Slide", "timestamp": "10:05 AM", "status": "success"},
        ]
        super().__init__(parent)
        
    def setup_ui(self):
        super().setup_ui()
        
        # Title
        title_label = QLabel("Voice Command Control")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.main_layout.addWidget(title_label)
        
        subtitle = QLabel("Control your system using voice commands")
        subtitle.setStyleSheet("color: #B0B0B0;")
        self.main_layout.addWidget(subtitle)
        
        # Main content layout (grid with voice control and history)
        content_layout = QGridLayout()
        
        # Voice control card
        voice_control = QFrame()
        voice_control.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
        """)
        
        vc_layout = QVBoxLayout(voice_control)
        
        # Header with title and status
        header_layout = QHBoxLayout()
        vc_title = QLabel("Voice Recognition")
        vc_title.setFont(QFont("Arial", 14, QFont.Bold))
        
        self.status_label = QLabel("Idle")
        self.status_label.setStyleSheet("""
            background-color: transparent;
            color: #B0B0B0;
            border: 1px solid #B0B0B0;
            border-radius: 10px;
            padding: 2px 8px;
        """)
        
        header_layout.addWidget(vc_title)
        header_layout.addStretch()
        header_layout.addWidget(self.status_label)
        
        vc_layout.addLayout(header_layout)
        
        # Voice button and visualizer
        vc_center_layout = QVBoxLayout()
        vc_center_layout.setAlignment(Qt.AlignCenter)
        
        self.voice_button = QPushButton()
        self.voice_button.setFixedSize(80, 80)
        self.voice_button.setStyleSheet("""
            QPushButton {
                background-color: #6D28D9;
                border-radius: 40px;
                color: white;
                font-size: 24px;
            }
            QPushButton:hover {
                background-color: #5B21B6;
            }
        """)
        self.voice_button.setText("🎤")
        self.voice_button.clicked.connect(self.toggle_listening)
        
        vc_center_layout.addWidget(self.voice_button, alignment=Qt.AlignCenter)
        
        # Voice visualizer
        self.visualizer = VoiceVisualizer()
        vc_center_layout.addWidget(self.visualizer)
        
        # Recognized text area
        self.text_area = QFrame()
        self.text_area.setStyleSheet("""
            QFrame {
                background-color: rgba(139, 92, 246, 0.1);
                border-radius: 5px;
                min-height: 60px;
            }
        """)
        
        text_layout = QVBoxLayout(self.text_area)
        self.recognized_label = QLabel("Click the microphone to start")
        self.recognized_label.setAlignment(Qt.AlignCenter)
        self.recognized_label.setStyleSheet("color: #B0B0B0;")
        text_layout.addWidget(self.recognized_label)
        
        vc_center_layout.addWidget(self.text_area)
        vc_layout.addLayout(vc_center_layout)
        
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
        tips_title = QLabel("Voice Command Tips")
        tips_title.setFont(QFont("Arial", 10, QFont.Bold))
        
        tips_text = QLabel("Try commands like \"Open Browser\", \"Volume Up\", \"Close Window\", or \"Scroll Down\" to control your system.")
        tips_text.setWordWrap(True)
        tips_text.setStyleSheet("color: #B0B0B0;")
        
        tips_content.addWidget(tips_title)
        tips_content.addWidget(tips_text)
        
        tips_layout.addWidget(tips_icon)
        tips_layout.addLayout(tips_content)
        
        vc_layout.addWidget(tips_frame)
        
        # Add voice control to content layout
        content_layout.addWidget(voice_control, 0, 0, 1, 2)
        
        # Command history
        history_widget = CommandHistory(self.commands)
        content_layout.addWidget(history_widget, 0, 2)
        
        content_layout.setColumnStretch(0, 2)
        content_layout.setColumnStretch(2, 1)
        
        self.main_layout.addLayout(content_layout)
        
    def toggle_listening(self):
        """Toggle the voice listening state"""
        self.is_listening = not self.is_listening
        
        if self.is_listening:
            self.voice_button.setStyleSheet("""
                QPushButton {
                    background-color: #EF4444;
                    border-radius: 40px;
                    color: white;
                    font-size: 24px;
                }
                QPushButton:hover {
                    background-color: #DC2626;
                }
            """)
            self.status_label.setText("Listening")
            self.status_label.setStyleSheet("""
                background-color: #8B5CF6;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 2px 8px;
            """)
            self.recognized_label.setText("Listening...")
            
            # Here would be the code to activate speech recognition
            # For now, we'll just simulate with the visualizer
            self.visualizer.set_active(True)
        else:
            self.voice_button.setStyleSheet("""
                QPushButton {
                    background-color: #6D28D9;
                    border-radius: 40px;
                    color: white;
                    font-size: 24px;
                }
                QPushButton:hover {
                    background-color: #5B21B6;
                }
            """)
            self.status_label.setText("Idle")
            self.status_label.setStyleSheet("""
                background-color: transparent;
                color: #B0B0B0;
                border: 1px solid #B0B0B0;
                border-radius: 10px;
                padding: 2px 8px;
            """)
            self.recognized_label.setText("Click the microphone to start")
            self.visualizer.set_active(False)
