
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                           QGridLayout, QFrame, QSlider, QComboBox, QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from views.base_view import BaseView

class SettingGroup(QFrame):
    """Group of related settings"""
    
    def __init__(self, title, description, icon, parent=None):
        super().__init__(parent)
        self.title = title
        self.description = description
        self.icon = icon
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
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: #1A1F2C;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #8B5CF6;
                border: 1px solid #5B21B6;
                width: 18px;
                border-radius: 9px;
                margin: -5px 0;
            }
            QSlider::sub-page:horizontal {
                background: #8B5CF6;
                border-radius: 4px;
            }
            QComboBox {
                background-color: #1A1F2C;
                border: 1px solid #3A3F4C;
                border-radius: 4px;
                color: white;
                padding: 4px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url();
                width: 0px;
                height: 0px;
            }
            QComboBox QAbstractItemView {
                background-color: #1A1F2C;
                border: 1px solid #3A3F4C;
                selection-background-color: #8B5CF6;
                color: white;
            }
            QCheckBox {
                color: white;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 4px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #6B7280;
                background: #1A1F2C;
            }
            QCheckBox::indicator:checked {
                background: #8B5CF6;
                border: 2px solid #8B5CF6;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Header
        header_layout = QHBoxLayout()
        icon_label = QLabel(self.icon)
        
        title_layout = QVBoxLayout()
        title_label = QLabel(self.title)
        title_label.setFont(QFont("Arial", 12, QFont.Bold))
        
        desc_label = QLabel(self.description)
        desc_label.setStyleSheet("color: #B0B0B0; font-size: 8pt;")
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(desc_label)
        
        header_layout.addWidget(icon_label)
        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        
        layout.addLayout(header_layout)
        
        # Content area for child widgets
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(10, 10, 10, 10)
        
        layout.addLayout(self.content_layout)
        self.setLayout(layout)
        
    def add_toggle_setting(self, label, description, default_checked=False):
        """Add a toggle switch setting"""
        setting_layout = QVBoxLayout()
        
        # Label and description
        label_layout = QHBoxLayout()
        setting_label = QLabel(label)
        setting_label.setFont(QFont("Arial", 10))
        
        toggle = QCheckBox()
        toggle.setChecked(default_checked)
        
        label_layout.addWidget(setting_label)
        label_layout.addStretch()
        label_layout.addWidget(toggle)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setStyleSheet("color: #B0B0B0; font-size: 8pt;")
        
        setting_layout.addLayout(label_layout)
        setting_layout.addWidget(desc_label)
        
        self.content_layout.addLayout(setting_layout)
        self.content_layout.addSpacing(10)
        
        return toggle
        
    def add_slider_setting(self, label, min_val=0, max_val=100, default_value=50):
        """Add a slider setting"""
        setting_layout = QVBoxLayout()
        
        # Label
        label_layout = QHBoxLayout()
        setting_label = QLabel(label)
        
        value_label = QLabel(f"{default_value}")
        
        label_layout.addWidget(setting_label)
        label_layout.addStretch()
        label_layout.addWidget(value_label)
        
        # Slider
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(default_value)
        
        # Connect slider value change to update the value label
        slider.valueChanged.connect(lambda val: value_label.setText(f"{val}"))
        
        setting_layout.addLayout(label_layout)
        setting_layout.addWidget(slider)
        
        self.content_layout.addLayout(setting_layout)
        self.content_layout.addSpacing(10)
        
        return slider
        
    def add_select_setting(self, label, options, default_value=None):
        """Add a select/dropdown setting"""
        setting_layout = QVBoxLayout()
        
        # Label
        setting_label = QLabel(label)
        
        # Combo box
        combo = QComboBox()
        for option in options:
            combo.addItem(option['label'], option['value'])
            
        # Set default if provided
        if default_value:
            index = combo.findData(default_value)
            if index >= 0:
                combo.setCurrentIndex(index)
        
        setting_layout.addWidget(setting_label)
        setting_layout.addWidget(combo)
        
        self.content_layout.addLayout(setting_layout)
        self.content_layout.addSpacing(10)
        
        return combo


class SettingsView(BaseView):
    """Settings view for the application"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def setup_ui(self):
        super().setup_ui()
        
        # Title
        title_label = QLabel("Settings")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.main_layout.addWidget(title_label)
        
        subtitle = QLabel("Customize your GAMINATOR experience")
        subtitle.setStyleSheet("color: #B0B0B0;")
        self.main_layout.addWidget(subtitle)
        
        # Settings grid layout
        settings_layout = QGridLayout()
        
        # Voice Command Settings
        voice_settings = SettingGroup("Voice Command Settings", 
                                      "Configure voice recognition options", 
                                      "🎤")
        
        voice_settings.add_toggle_setting("Enable Voice Commands", 
                                         "Turn voice command recognition on or off", 
                                         True)
        
        voice_settings.add_slider_setting("Microphone Sensitivity", 0, 100, 75)
        
        lang_options = [
            {"value": "en-US", "label": "English (US)"},
            {"value": "en-UK", "label": "English (UK)"},
            {"value": "es", "label": "Spanish"},
            {"value": "fr", "label": "French"},
            {"value": "de", "label": "German"}
        ]
        voice_settings.add_select_setting("Language", lang_options, "en-US")
        
        voice_settings.add_toggle_setting("Continuous Listening", 
                                         "Keep listening for commands without manually activating", 
                                         False)
        
        # Gesture Control Settings
        gesture_settings = SettingGroup("Gesture Control Settings", 
                                        "Configure hand gesture recognition options", 
                                        "👋")
        
        gesture_settings.add_toggle_setting("Enable Gesture Control", 
                                           "Turn hand gesture recognition on or off", 
                                           True)
        
        camera_options = [
            {"value": "default", "label": "Default Camera"},
            {"value": "usb", "label": "USB Camera"},
            {"value": "external", "label": "External Webcam"}
        ]
        gesture_settings.add_select_setting("Camera Source", camera_options, "default")
        
        gesture_settings.add_slider_setting("Detection Sensitivity", 0, 100, 65)
        
        gesture_settings.add_toggle_setting("Show Hand Skeleton", 
                                          "Display skeletal tracking on detected hands", 
                                          True)
        
        # System Settings
        system_settings = SettingGroup("System Settings", 
                                      "Configure general system behavior", 
                                      "💻")
        
        system_settings.add_toggle_setting("Start with System", 
                                          "Launch application when computer starts", 
                                          False)
        
        system_settings.add_toggle_setting("Run in Background", 
                                         "Keep program running in the system tray", 
                                         True)
        
        theme_options = [
            {"value": "system", "label": "System Default"},
            {"value": "dark", "label": "Dark Mode"},
            {"value": "light", "label": "Light Mode"}
        ]
        system_settings.add_select_setting("Interface Theme", theme_options, "dark")
        
        system_settings.add_slider_setting("UI Animation Speed", 0, 100, 80)
        
        # Notification Settings
        notification_settings = SettingGroup("Notification Settings", 
                                            "Configure alerts and feedback", 
                                            "🔔")
        
        notification_settings.add_toggle_setting("Sound Feedback", 
                                               "Play sounds on command recognition", 
                                               True)
        
        notification_settings.add_toggle_setting("Visual Notifications", 
                                               "Show on-screen notifications for actions", 
                                               True)
        
        notification_settings.add_slider_setting("Notification Duration", 1, 10, 3)
        
        position_options = [
            {"value": "top-right", "label": "Top Right"},
            {"value": "top-left", "label": "Top Left"},
            {"value": "bottom-right", "label": "Bottom Right"},
            {"value": "bottom-left", "label": "Bottom Left"}
        ]
        notification_settings.add_select_setting("Notification Position", position_options, "top-right")
        
        # Add all setting groups to the grid
        settings_layout.addWidget(voice_settings, 0, 0)
        settings_layout.addWidget(gesture_settings, 0, 1)
        settings_layout.addWidget(system_settings, 1, 0)
        settings_layout.addWidget(notification_settings, 1, 1)
        
        self.main_layout.addLayout(settings_layout)
