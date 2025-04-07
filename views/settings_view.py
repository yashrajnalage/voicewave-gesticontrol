
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
                             QCheckBox, QSlider, QComboBox)
from PyQt5.QtCore import Qt
from views.base_view import BaseView

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
        voice_settings = self.create_settings_section("Voice Command Settings", "Configure voice recognition options")
        
        # Add settings to the voice section
        voice_enable = QCheckBox("Enable Voice Commands")
        voice_enable.setChecked(True)
        voice_enable_desc = QLabel("Turn voice command recognition on or off")
        voice_enable_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        voice_sensitivity_label = QLabel("Microphone Sensitivity")
        voice_sensitivity = QSlider(Qt.Horizontal)
        voice_sensitivity.setValue(75)
        
        voice_language_label = QLabel("Language")
        voice_language = QComboBox()
        voice_language.addItems(["English (US)", "English (UK)", "Spanish", "French", "German"])
        
        continuous_listening = QCheckBox("Continuous Listening")
        continuous_listening.setChecked(False)
        continuous_listening_desc = QLabel("Keep listening for commands without manually activating")
        continuous_listening_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        voice_layout = QVBoxLayout()
        voice_layout.addWidget(voice_enable)
        voice_layout.addWidget(voice_enable_desc)
        voice_layout.addSpacing(10)
        voice_layout.addWidget(voice_sensitivity_label)
        voice_layout.addWidget(voice_sensitivity)
        voice_layout.addSpacing(10)
        voice_layout.addWidget(voice_language_label)
        voice_layout.addWidget(voice_language)
        voice_layout.addSpacing(10)
        voice_layout.addWidget(continuous_listening)
        voice_layout.addWidget(continuous_listening_desc)
        
        voice_settings.layout().addLayout(voice_layout)
        
        # System settings
        system_settings = self.create_settings_section("System Settings", "Configure general system behavior")
        
        start_with_system = QCheckBox("Start with System")
        start_with_system.setChecked(False)
        start_desc = QLabel("Launch application when computer starts")
        start_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        run_bg = QCheckBox("Run in Background")
        run_bg.setChecked(True)
        run_bg_desc = QLabel("Keep program running in the system tray")
        run_bg_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        theme_label = QLabel("Interface Theme")
        theme = QComboBox()
        theme.addItems(["System Default", "Dark Mode", "Light Mode"])
        theme.setCurrentIndex(1)  # Dark mode selected
        
        animation_label = QLabel("UI Animation Speed")
        animation = QSlider(Qt.Horizontal)
        animation.setValue(80)
        
        system_layout = QVBoxLayout()
        system_layout.addWidget(start_with_system)
        system_layout.addWidget(start_desc)
        system_layout.addSpacing(10)
        system_layout.addWidget(run_bg)
        system_layout.addWidget(run_bg_desc)
        system_layout.addSpacing(10)
        system_layout.addWidget(theme_label)
        system_layout.addWidget(theme)
        system_layout.addSpacing(10)
        system_layout.addWidget(animation_label)
        system_layout.addWidget(animation)
        
        system_settings.layout().addLayout(system_layout)
        
        # Add sections to left column
        left_layout.addWidget(voice_settings)
        left_layout.addWidget(system_settings)
        
        # Right column
        right_layout = QVBoxLayout()
        
        # Gesture settings
        gesture_settings = self.create_settings_section("Gesture Control Settings", "Configure hand gesture recognition options")
        
        gesture_enable = QCheckBox("Enable Gesture Control")
        gesture_enable.setChecked(True)
        gesture_enable_desc = QLabel("Turn hand gesture recognition on or off")
        gesture_enable_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        camera_label = QLabel("Camera Source")
        camera = QComboBox()
        camera.addItems(["Default Camera", "USB Camera", "External Webcam"])
        
        gesture_sensitivity_label = QLabel("Detection Sensitivity")
        gesture_sensitivity = QSlider(Qt.Horizontal)
        gesture_sensitivity.setValue(65)
        
        show_skeleton = QCheckBox("Show Hand Skeleton")
        show_skeleton.setChecked(True)
        skeleton_desc = QLabel("Display skeletal tracking on detected hands")
        skeleton_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        gesture_layout = QVBoxLayout()
        gesture_layout.addWidget(gesture_enable)
        gesture_layout.addWidget(gesture_enable_desc)
        gesture_layout.addSpacing(10)
        gesture_layout.addWidget(camera_label)
        gesture_layout.addWidget(camera)
        gesture_layout.addSpacing(10)
        gesture_layout.addWidget(gesture_sensitivity_label)
        gesture_layout.addWidget(gesture_sensitivity)
        gesture_layout.addSpacing(10)
        gesture_layout.addWidget(show_skeleton)
        gesture_layout.addWidget(skeleton_desc)
        
        gesture_settings.layout().addLayout(gesture_layout)
        
        # Notification settings
        notification_settings = self.create_settings_section("Notification Settings", "Configure alerts and feedback")
        
        sound_feedback = QCheckBox("Sound Feedback")
        sound_feedback.setChecked(True)
        sound_desc = QLabel("Play sounds on command recognition")
        sound_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        visual_notif = QCheckBox("Visual Notifications")
        visual_notif.setChecked(True)
        visual_desc = QLabel("Show on-screen notifications for actions")
        visual_desc.setStyleSheet("color: #888; font-size: 12px;")
        
        duration_label = QLabel("Notification Duration")
        duration = QSlider(Qt.Horizontal)
        duration.setMinimum(1)
        duration.setMaximum(10)
        duration.setValue(3)
        
        position_label = QLabel("Notification Position")
        position = QComboBox()
        position.addItems(["Top Right", "Top Left", "Bottom Right", "Bottom Left"])
        
        notif_layout = QVBoxLayout()
        notif_layout.addWidget(sound_feedback)
        notif_layout.addWidget(sound_desc)
        notif_layout.addSpacing(10)
        notif_layout.addWidget(visual_notif)
        notif_layout.addWidget(visual_desc)
        notif_layout.addSpacing(10)
        notif_layout.addWidget(duration_label)
        notif_layout.addWidget(duration)
        notif_layout.addSpacing(10)
        notif_layout.addWidget(position_label)
        notif_layout.addWidget(position)
        
        notification_settings.layout().addLayout(notif_layout)
        
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
    
    def create_settings_section(self, title, desc):
        """Create a settings section with the given title and description"""
        section = QWidget()
        section.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 15px;")
        
        section_layout = QVBoxLayout(section)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        section_layout.addWidget(title_label)
        
        desc_label = QLabel(desc)
        desc_label.setStyleSheet("color: #888; font-size: 12px;")
        section_layout.addWidget(desc_label)
        
        section_layout.addSpacing(10)
        
        return section
