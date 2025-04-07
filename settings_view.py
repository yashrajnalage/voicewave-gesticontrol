
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
                             QCheckBox, QSlider, QComboBox)
from PyQt5.QtCore import Qt
from base_view import BaseView

class SettingsCard(QWidget):
    """Widget for grouping related settings"""
    def __init__(self, title, description, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 15px;")
        
        self.layout = QVBoxLayout(self)
        
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.title_label)
        
        self.desc_label = QLabel(description)
        self.desc_label.setStyleSheet("color: #888; font-size: 12px;")
        self.layout.addWidget(self.desc_label)
        
        self.layout.addSpacing(10)
    
    def add_option(self, option_widget, description=None):
        """Add a setting option with optional description"""
        self.layout.addWidget(option_widget)
        
        if description:
            desc_label = QLabel(description)
            desc_label.setStyleSheet("color: #888; font-size: 12px;")
            self.layout.addWidget(desc_label)
        
        self.layout.addSpacing(10)


class SettingsView(BaseView):
    """View for application settings"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def setup_ui(self):
        """Set up the UI components"""
        super().setup_ui()
        
        # Main title
        title_label = QLabel("Settings")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Customize your GAMINATOR experience")
        subtitle_label.setStyleSheet("font-size: 14px; color: #888;")
        self.main_layout.addWidget(subtitle_label)
        
        # Settings layout with two columns
        settings_layout = QHBoxLayout()
        
        # Left column
        left_layout = QVBoxLayout()
        
        # Voice command settings
        voice_settings = SettingsCard("Voice Command Settings", "Configure voice recognition options")
        
        voice_enable = QCheckBox("Enable Voice Commands")
        voice_enable.setChecked(True)
        voice_settings.add_option(voice_enable, "Turn voice command recognition on or off")
        
        voice_sensitivity_label = QLabel("Microphone Sensitivity")
        voice_settings.add_option(voice_sensitivity_label)
        
        voice_sensitivity = QSlider(Qt.Horizontal)
        voice_sensitivity.setValue(75)
        voice_settings.add_option(voice_sensitivity)
        
        voice_language_label = QLabel("Language")
        voice_settings.add_option(voice_language_label)
        
        voice_language = QComboBox()
        voice_language.addItems(["English (US)", "English (UK)", "Spanish", "French", "German"])
        voice_settings.add_option(voice_language)
        
        continuous_listening = QCheckBox("Continuous Listening")
        continuous_listening.setChecked(False)
        voice_settings.add_option(continuous_listening, "Keep listening for commands without manually activating")
        
        # System settings
        system_settings = SettingsCard("System Settings", "Configure general system behavior")
        
        start_with_system = QCheckBox("Start with System")
        start_with_system.setChecked(False)
        system_settings.add_option(start_with_system, "Launch application when computer starts")
        
        run_bg = QCheckBox("Run in Background")
        run_bg.setChecked(True)
        system_settings.add_option(run_bg, "Keep program running in the system tray")
        
        theme_label = QLabel("Interface Theme")
        system_settings.add_option(theme_label)
        
        theme = QComboBox()
        theme.addItems(["System Default", "Dark Mode", "Light Mode"])
        theme.setCurrentIndex(1)  # Dark mode selected
        system_settings.add_option(theme)
        
        # Add sections to left column
        left_layout.addWidget(voice_settings)
        left_layout.addWidget(system_settings)
        
        # Right column
        right_layout = QVBoxLayout()
        
        # Gesture settings
        gesture_settings = SettingsCard("Gesture Control Settings", "Configure hand gesture recognition options")
        
        gesture_enable = QCheckBox("Enable Gesture Control")
        gesture_enable.setChecked(True)
        gesture_settings.add_option(gesture_enable, "Turn hand gesture recognition on or off")
        
        camera_label = QLabel("Camera Source")
        gesture_settings.add_option(camera_label)
        
        camera = QComboBox()
        camera.addItems(["Default Camera", "USB Camera", "External Webcam"])
        gesture_settings.add_option(camera)
        
        gesture_sensitivity_label = QLabel("Detection Sensitivity")
        gesture_settings.add_option(gesture_sensitivity_label)
        
        gesture_sensitivity = QSlider(Qt.Horizontal)
        gesture_sensitivity.setValue(65)
        gesture_settings.add_option(gesture_sensitivity)
        
        show_skeleton = QCheckBox("Show Hand Skeleton")
        show_skeleton.setChecked(True)
        gesture_settings.add_option(show_skeleton, "Display skeletal tracking on detected hands")
        
        # Notification settings
        notification_settings = SettingsCard("Notification Settings", "Configure alerts and feedback")
        
        sound_feedback = QCheckBox("Sound Feedback")
        sound_feedback.setChecked(True)
        notification_settings.add_option(sound_feedback, "Play sounds on command recognition")
        
        visual_notif = QCheckBox("Visual Notifications")
        visual_notif.setChecked(True)
        notification_settings.add_option(visual_notif, "Show on-screen notifications for actions")
        
        # Add sections to right column
        right_layout.addWidget(gesture_settings)
        right_layout.addWidget(notification_settings)
        
        # Add columns to settings layout
        settings_layout.addLayout(left_layout)
        settings_layout.addLayout(right_layout)
        
        self.main_layout.addLayout(settings_layout)
        
        self.main_layout.addStretch()
        
        # Add navigation bar at the bottom
        self.main_layout.addLayout(self.nav_layout)
