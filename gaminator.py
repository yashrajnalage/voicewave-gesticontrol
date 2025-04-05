
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

from views.home_view import HomeView
from views.voice_command_view import VoiceCommandView
from views.gesture_control_view import GestureControlView
from views.dashboard_view import DashboardView
from views.settings_view import SettingsView

class Gaminator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GAMINATOR")
        self.setMinimumSize(1000, 700)
        
        # Create a stacked widget to handle different views/pages
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialize views
        self.home_view = HomeView(self)
        self.voice_command_view = VoiceCommandView(self)
        self.gesture_control_view = GestureControlView(self)
        self.dashboard_view = DashboardView(self)
        self.settings_view = SettingsView(self)
        
        # Add views to stacked widget
        self.stacked_widget.addWidget(self.home_view)
        self.stacked_widget.addWidget(self.voice_command_view)
        self.stacked_widget.addWidget(self.gesture_control_view)
        self.stacked_widget.addWidget(self.dashboard_view)
        self.stacked_widget.addWidget(self.settings_view)
        
        # Set the initial view to home
        self.stacked_widget.setCurrentWidget(self.home_view)
        
        # Set dark theme
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1A1F2C;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #8B5CF6;
                color: white;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7C3AED;
            }
            QLabel {
                color: #FFFFFF;
            }
        """)

    def navigate_to(self, view_name):
        """Navigate to a specific view by name"""
        if view_name == "home":
            self.stacked_widget.setCurrentWidget(self.home_view)
        elif view_name == "voice":
            self.stacked_widget.setCurrentWidget(self.voice_command_view)
        elif view_name == "gesture":
            self.stacked_widget.setCurrentWidget(self.gesture_control_view)
        elif view_name == "dashboard":
            self.stacked_widget.setCurrentWidget(self.dashboard_view)
        elif view_name == "settings":
            self.stacked_widget.setCurrentWidget(self.settings_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use Fusion style for a more modern look
    
    window = Gaminator()
    window.show()
    
    sys.exit(app.exec_())
