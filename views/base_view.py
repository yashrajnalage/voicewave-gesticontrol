
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

class BaseView(QWidget):
    """Base class for all views in the application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the UI components - to be implemented by subclasses"""
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)
        
        # Add navigation bar at the bottom
        self.create_navigation_bar()
        
    def create_navigation_bar(self):
        """Create the bottom navigation bar"""
        nav_layout = QHBoxLayout()
        
        # Create navigation buttons
        home_btn = self.create_nav_button("Home", "home")
        voice_btn = self.create_nav_button("Voice", "voice")
        gesture_btn = self.create_nav_button("Gesture", "gesture")
        dashboard_btn = self.create_nav_button("Dashboard", "dashboard")
        settings_btn = self.create_nav_button("Settings", "settings")
        
        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(voice_btn)
        nav_layout.addWidget(gesture_btn)
        nav_layout.addWidget(dashboard_btn)
        nav_layout.addWidget(settings_btn)
        
        self.main_layout.addLayout(nav_layout)
        
    def create_nav_button(self, text, view_name):
        """Create a navigation button with text and connect it to navigation function"""
        button = QPushButton(text)
        button.clicked.connect(lambda: self.navigate_to(view_name))
        button.setFixedHeight(50)
        button.setMinimumWidth(100)
        return button
        
    def navigate_to(self, view_name):
        """Navigate to a different view using the parent's navigate_to method"""
        if self.parent:
            self.parent.navigate_to(view_name)
