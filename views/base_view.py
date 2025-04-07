
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

class BaseView(QWidget):
    """Base class for all views"""
    
    # Signal for navigation between views
    navigate_signal = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the UI components common to all views"""
        # Navigation bar at the bottom
        self.nav_layout = QHBoxLayout()
        
        # Navigation buttons
        self.home_button = QPushButton("Home")
        self.voice_button = QPushButton("Voice")
        self.gesture_button = QPushButton("Gesture")
        self.dashboard_button = QPushButton("Dashboard")
        self.settings_button = QPushButton("Settings")
        
        # Add buttons to navigation bar
        self.nav_layout.addWidget(self.home_button)
        self.nav_layout.addWidget(self.voice_button)
        self.nav_layout.addWidget(self.gesture_button)
        self.nav_layout.addWidget(self.dashboard_button)
        self.nav_layout.addWidget(self.settings_button)
        
        # Connect navigation signals
        self.home_button.clicked.connect(lambda: self.navigate_signal.emit("home"))
        self.voice_button.clicked.connect(lambda: self.navigate_signal.emit("voice"))
        self.gesture_button.clicked.connect(lambda: self.navigate_signal.emit("gesture"))
        self.dashboard_button.clicked.connect(lambda: self.navigate_signal.emit("dashboard"))
        self.settings_button.clicked.connect(lambda: self.navigate_signal.emit("settings"))
        
        # Add navigation bar to the bottom of the layout
        # This will be added at the end of each view's setup
