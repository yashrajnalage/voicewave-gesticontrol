
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
                             QCheckBox, QSlider, QComboBox, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from base_view import BaseView

class SettingsCard(QWidget):
    """Widget for grouping related settings"""
    def __init__(self, title, description=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget#settingsCard {
                background-color: #262c3b;
                border-radius: 8px;
                padding: 15px;
                margin-bottom: 10px;
            }
            QLabel#cardTitle {
                font-size: 16px;
                font-weight: bold;
                color: white;
            }
            QLabel#cardDesc {
                color: #aaadb0;
                font-size: 12px;
            }
            QCheckBox {
                color: white;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #555;
                background: #1A1F2C;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                border: 2px solid #8B5CF6;
                background: #8B5CF6;
                border-radius: 3px;
            }
            QLabel#optionDesc {
                color: #888;
                font-size: 12px;
                padding-left: 24px;
                margin-top: -5px;
            }
        """)
        self.setObjectName("settingsCard")
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(5)
        
        self.title_label = QLabel(title)
        self.title_label.setObjectName("cardTitle")
        font = QFont()
        font.setBold(True)
        self.title_label.setFont(font)
        self.layout.addWidget(self.title_label)
        
        if description:
            self.desc_label = QLabel(description)
            self.desc_label.setObjectName("cardDesc")
            self.layout.addWidget(self.desc_label)
        
        self.layout.addSpacing(10)
        
    def add_checkbox_option(self, label, description=None, checked=False):
        """Add a checkbox option with optional description"""
        checkbox = QCheckBox(label)
        checkbox.setChecked(checked)
        self.layout.addWidget(checkbox)
        
        if description:
            desc_label = QLabel(description)
            desc_label.setObjectName("optionDesc")
            self.layout.addWidget(desc_label)
            self.layout.addSpacing(8)
        else:
            self.layout.addSpacing(4)
            
        return checkbox
    
    def add_slider_option(self, label, min_value=0, max_value=100, default_value=50):
        """Add a slider option with label"""
        label_layout = QHBoxLayout()
        slider_label = QLabel(label)
        value_label = QLabel(f"{default_value}%")
        value_label.setAlignment(Qt.AlignRight)
        label_layout.addWidget(slider_label)
        label_layout.addWidget(value_label)
        
        self.layout.addLayout(label_layout)
        
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)
        slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #444;
                height: 8px;
                background: #2A2F3C;
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #8B5CF6;
                border: 1px solid #8B5CF6;
                width: 18px;
                margin: -2px 0;
                border-radius: 9px;
            }
        """)
        
        self.layout.addWidget(slider)
        self.layout.addSpacing(10)
        
        # Update value label when slider changes
        slider.valueChanged.connect(lambda v: value_label.setText(f"{v}%"))
        
        return slider
    
    def add_select_option(self, label, options):
        """Add a dropdown select option"""
        select_label = QLabel(label)
        self.layout.addWidget(select_label)
        
        select = QComboBox()
        select.addItems(options)
        select.setStyleSheet("""
            QComboBox {
                background-color: #2A2F3C;
                color: white;
                border: 1px solid #444;
                border-radius: 5px;
                padding: 5px;
                min-width: 6em;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: #444;
                border-left-style: solid;
            }
        """)
        
        self.layout.addWidget(select)
        self.layout.addSpacing(10)
        
        return select


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
        subtitle_label.setStyleSheet("font-size: 14px; color: #aaadb0; margin-bottom: 20px;")
        self.main_layout.addWidget(subtitle_label)
        
        # Settings layout with two columns
        settings_layout = QHBoxLayout()
        settings_layout.setSpacing(20)
        
        # Left column
        left_layout = QVBoxLayout()
        
        # Voice command settings
        voice_settings = SettingsCard("Voice Command Settings", "Configure voice recognition options")
        
        voice_enable = voice_settings.add_checkbox_option(
            "Enable Voice Commands", 
            "Turn voice command recognition on or off",
            True
        )
        
        mic_sensitivity = voice_settings.add_slider_option("Microphone Sensitivity", 0, 100, 75)
        
        language_select = voice_settings.add_select_option(
            "Language",
            ["English (US)", "English (UK)", "Spanish", "French", "German"]
        )
        
        continuous_listening = voice_settings.add_checkbox_option(
            "Continuous Listening",
            "Keep listening for commands without manually activating",
            False
        )
        
        # System settings
        system_settings = SettingsCard("System Settings", "Configure general system behavior")
        
        start_with_system = system_settings.add_checkbox_option(
            "Start with System",
            "Launch application when computer starts",
            False
        )
        
        run_bg = system_settings.add_checkbox_option(
            "Run in Background",
            "Keep program running in the system tray",
            True
        )
        
        theme_select = system_settings.add_select_option(
            "Interface Theme",
            ["System Default", "Dark Mode", "Light Mode"]
        )
        theme_select.setCurrentIndex(1)  # Set to Dark Mode
        
        animation_speed = system_settings.add_slider_option("UI Animation Speed", 0, 100, 80)
        
        # Add sections to left column
        left_layout.addWidget(voice_settings)
        left_layout.addWidget(system_settings)
        left_layout.addStretch()
        
        # Right column
        right_layout = QVBoxLayout()
        
        # Gesture settings
        gesture_settings = SettingsCard("Gesture Control Settings", "Configure hand gesture recognition options")
        
        gesture_enable = gesture_settings.add_checkbox_option(
            "Enable Gesture Control",
            "Turn hand gesture recognition on or off",
            True
        )
        
        camera_select = gesture_settings.add_select_option(
            "Camera Source",
            ["Default Camera", "USB Camera", "External Webcam"]
        )
        
        gesture_sensitivity = gesture_settings.add_slider_option("Detection Sensitivity", 0, 100, 65)
        
        show_skeleton = gesture_settings.add_checkbox_option(
            "Show Hand Skeleton",
            "Display skeletal tracking on detected hands",
            True
        )
        
        # Notification settings
        notification_settings = SettingsCard("Notification Settings", "Configure alerts and feedback")
        
        sound_feedback = notification_settings.add_checkbox_option(
            "Sound Feedback",
            "Play sounds on command recognition",
            True
        )
        
        visual_notif = notification_settings.add_checkbox_option(
            "Visual Notifications",
            "Show on-screen notifications for actions",
            True
        )
        
        duration_slider = notification_settings.add_slider_option("Notification Duration", 1, 10, 3)
        
        position_select = notification_settings.add_select_option(
            "Notification Position",
            ["Top Right", "Top Left", "Bottom Right", "Bottom Left"]
        )
        
        # Add sections to right column
        right_layout.addWidget(gesture_settings)
        right_layout.addWidget(notification_settings)
        right_layout.addStretch()
        
        # Add columns to settings layout
        settings_layout.addLayout(left_layout)
        settings_layout.addLayout(right_layout)
        
        # Add settings layout to main layout
        self.main_layout.addLayout(settings_layout)
        self.main_layout.addStretch()
        
        # Add navigation bar at the bottom
        self.main_layout.addLayout(self.nav_layout)
