
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                           QGridLayout, QFrame)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QFont, QColor
from views.base_view import BaseView

class FeatureCard(QFrame):
    """A card widget for displaying features on the home page"""
    
    def __init__(self, title, description, icon_text, parent=None):
        super().__init__(parent)
        self.title = title
        self.description = description
        self.icon_text = icon_text
        self.setup_ui()
        
    def setup_ui(self):
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: transparent;
                border: 1px solid #8B5CF6;
                border-radius: 5px;
                color: #8B5CF6;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #8B5CF6;
                color: white;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Icon container
        icon_container = QFrame()
        icon_container.setStyleSheet("""
            QFrame {
                background-color: rgba(139, 92, 246, 0.2);
                border-radius: 25px;
                max-width: 50px;
                max-height: 50px;
                min-width: 50px;
                min-height: 50px;
            }
        """)
        icon_layout = QVBoxLayout(icon_container)
        
        icon = QLabel(self.icon_text)
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet("color: #8B5CF6; font-size: 24px;")
        
        icon_layout.addWidget(icon)
        layout.addWidget(icon_container, alignment=Qt.AlignCenter)
        
        # Title
        title_label = QLabel(self.title)
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel(self.description)
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet("color: #B0B0B0;")
        layout.addWidget(desc_label)
        
        # Button
        button = QPushButton(f"Try {self.title}")
        layout.addWidget(button, alignment=Qt.AlignCenter)
        
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

class HomeView(BaseView):
    """Home view for the application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def setup_ui(self):
        super().setup_ui()
        
        # Title
        title_label = QLabel("Welcome to GAMINATOR")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            background: -webkit-linear-gradient(#3B82F6, #0EA5E9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        """)
        self.main_layout.addWidget(title_label)
        
        # Subtitle
        subtitle = QLabel("Control your computer with voice and gesture commands")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #B0B0B0;")
        self.main_layout.addWidget(subtitle)
        
        # Feature cards
        cards_layout = QGridLayout()
        
        voice_card = FeatureCard(
            "Voice Commands",
            "Control your computer using simple voice commands for navigation, application control, and system functions.",
            "🎤"
        )
        
        gesture_card = FeatureCard(
            "Gesture Control",
            "Use hand gestures to navigate and interact with your applications without touching your keyboard or mouse.",
            "👋"
        )
        
        cards_layout.addWidget(voice_card, 0, 0)
        cards_layout.addWidget(gesture_card, 0, 1)
        
        self.main_layout.addLayout(cards_layout)
        
        # Getting started section
        getting_started_frame = QFrame()
        getting_started_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
            QLabel {
                color: white;
            }
        """)
        
        gs_layout = QVBoxLayout(getting_started_frame)
        
        gs_title = QLabel("Getting Started")
        gs_title.setFont(QFont("Arial", 14, QFont.Bold))
        gs_title.setAlignment(Qt.AlignCenter)
        gs_layout.addWidget(gs_title)
        
        gs_desc = QLabel("GAMINATOR allows you to control your computer without touching it. Try saying \"Open Browser\" or use a swipe gesture to navigate between apps.")
        gs_desc.setWordWrap(True)
        gs_desc.setAlignment(Qt.AlignCenter)
        gs_desc.setStyleSheet("color: #B0B0B0;")
        gs_layout.addWidget(gs_desc)
        
        gs_button = QPushButton("Go to Dashboard")
        gs_button.clicked.connect(lambda: self.navigate_to("dashboard"))
        gs_layout.addWidget(gs_button, alignment=Qt.AlignCenter)
        
        self.main_layout.addWidget(getting_started_frame)
        
        # Add spacer to push everything up
        self.main_layout.addStretch()
