
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from views.base_view import BaseView

class HomeView(BaseView):
    """View for the home screen"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def setup_ui(self):
        """Set up the UI components"""
        super().setup_ui()
        
        # Main title
        title_label = QLabel("Welcome to GAMINATOR")
        title_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #8B5CF6;")
        title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Control your computer with voice and gesture commands")
        subtitle_label.setStyleSheet("font-size: 16px; color: #888;")
        subtitle_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(subtitle_label)
        
        # Main content - Two feature cards
        features_layout = QHBoxLayout()
        
        # Voice commands card
        voice_card = QWidget()
        voice_layout = QVBoxLayout(voice_card)
        voice_title = QLabel("Voice Commands")
        voice_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        voice_desc = QLabel("Control your computer using simple voice commands\nfor navigation, application control, and system functions.")
        voice_desc.setWordWrap(True)
        voice_button = QPushButton("Try Voice Commands")
        voice_button.clicked.connect(lambda: self.navigate_signal.emit("voice"))
        
        voice_layout.addWidget(voice_title)
        voice_layout.addWidget(voice_desc)
        voice_layout.addStretch()
        voice_layout.addWidget(voice_button)
        voice_card.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 20px;")
        
        # Gesture control card
        gesture_card = QWidget()
        gesture_layout = QVBoxLayout(gesture_card)
        gesture_title = QLabel("Gesture Control")
        gesture_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        gesture_desc = QLabel("Use hand gestures to navigate and interact with your\napplications without touching your keyboard or mouse.")
        gesture_desc.setWordWrap(True)
        gesture_button = QPushButton("Try Gesture Control")
        gesture_button.clicked.connect(lambda: self.navigate_signal.emit("gesture"))
        
        gesture_layout.addWidget(gesture_title)
        gesture_layout.addWidget(gesture_desc)
        gesture_layout.addStretch()
        gesture_layout.addWidget(gesture_button)
        gesture_card.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 20px;")
        
        # Add cards to features layout
        features_layout.addWidget(voice_card)
        features_layout.addWidget(gesture_card)
        
        self.main_layout.addLayout(features_layout)
        
        # Getting started section
        getting_started = QWidget()
        gs_layout = QVBoxLayout(getting_started)
        gs_title = QLabel("Getting Started")
        gs_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        gs_desc = QLabel("GAMINATOR allows you to control your computer without touching it.\nTry saying \"Open Browser\" or use a swipe gesture to navigate between apps.")
        gs_desc.setAlignment(Qt.AlignCenter)
        gs_desc.setWordWrap(True)
        gs_button = QPushButton("Go to Dashboard")
        gs_button.clicked.connect(lambda: self.navigate_signal.emit("dashboard"))
        
        gs_layout.addWidget(gs_title)
        gs_layout.addWidget(gs_desc)
        gs_layout.addWidget(gs_button)
        getting_started.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 20px; margin-top: 20px;")
        
        self.main_layout.addWidget(getting_started)
        self.main_layout.addStretch()
        
        # Add navigation bar at the bottom
        self.main_layout.addLayout(self.nav_layout)
