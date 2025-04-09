
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
                             QCheckBox, QSlider, QComboBox, QPushButton)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QSize, QPoint
from PyQt5.QtGui import QFont, QColor
from base_view import BaseView

class SettingsCard(QWidget):
    """Widget for grouping related settings"""
    def __init__(self, title, description=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget#settingsCard {
                background-color: #262c3b;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 20px;
            }
            QLabel#cardTitle {
                font-size: 22px;
                font-weight: bold;
                color: white;
            }
            QLabel#cardDesc {
                color: #aaadb0;
                font-size: 16px;
            }
            QCheckBox {
                color: white;
                font-size: 18px;
            }
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #555;
                background: #1A1F2C;
                border-radius: 4px;
            }
            QCheckBox::indicator:checked {
                border: 2px solid #8B5CF6;
                background: #8B5CF6;
                border-radius: 4px;
            }
            QLabel#optionDesc {
                color: #888;
                font-size: 16px;
                padding-left: 32px;
                margin-top: -5px;
            }
        """)
        self.setObjectName("settingsCard")
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 25, 25, 25)
        self.layout.setSpacing(12)
        
        self.title_label = QLabel(title)
        self.title_label.setObjectName("cardTitle")
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.title_label.setFont(font)
        self.layout.addWidget(self.title_label)
        
        if description:
            self.desc_label = QLabel(description)
            self.desc_label.setObjectName("cardDesc")
            font = QFont()
            font.setPointSize(10)
            self.desc_label.setFont(font)
            self.layout.addWidget(self.desc_label)
        
        self.layout.addSpacing(20)
        
        # Animation properties
        self.is_expanded = True
        self.original_height = None
        self.animation = QPropertyAnimation(self, b"minimumHeight")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        
    def add_checkbox_option(self, label, description=None, checked=False):
        """Add a checkbox option with optional description"""
        checkbox = QCheckBox(label)
        checkbox.setChecked(checked)
        font = QFont()
        font.setPointSize(10)
        checkbox.setFont(font)
        self.layout.addWidget(checkbox)
        
        # Add animation to checkbox when state changes
        checkbox.stateChanged.connect(lambda: self.animate_checkbox(checkbox))
        
        if description:
            desc_label = QLabel(description)
            desc_label.setObjectName("optionDesc")
            font = QFont()
            font.setPointSize(9)
            desc_label.setFont(font)
            self.layout.addWidget(desc_label)
            self.layout.addSpacing(15)
        else:
            self.layout.addSpacing(10)
            
        return checkbox
    
    def add_slider_option(self, label, min_value=0, max_value=100, default_value=50):
        """Add a slider option with label"""
        label_layout = QHBoxLayout()
        slider_label = QLabel(label)
        slider_label.setStyleSheet("font-size: 18px;")
        value_label = QLabel(f"{default_value}%")
        value_label.setStyleSheet("font-size: 18px;")
        value_label.setAlignment(Qt.AlignRight)
        label_layout.addWidget(slider_label)
        label_layout.addWidget(value_label)
        
        self.layout.addLayout(label_layout)
        
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)
        slider.setFixedHeight(36)  # Make slider taller for better handling
        slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #444;
                height: 12px;
                background: #2A2F3C;
                margin: 2px 0;
                border-radius: 6px;
            }
            QSlider::handle:horizontal {
                background: #8B5CF6;
                border: 1px solid #8B5CF6;
                width: 26px;
                margin: -5px 0;
                border-radius: 13px;
            }
        """)
        
        self.layout.addWidget(slider)
        self.layout.addSpacing(20)
        
        # Add animation when slider value changes
        slider.valueChanged.connect(
            lambda v: self.animate_slider_change(v, value_label, slider))
        
        return slider
    
    def add_select_option(self, label, options):
        """Add a dropdown select option"""
        select_label = QLabel(label)
        select_label.setStyleSheet("font-size: 18px;")
        font = QFont()
        font.setPointSize(10)
        select_label.setFont(font)
        self.layout.addWidget(select_label)
        
        select = QComboBox()
        select.addItems(options)
        select.setFixedHeight(40)  # Make combobox taller for better usability
        select.setStyleSheet("""
            QComboBox {
                background-color: #2A2F3C;
                color: white;
                border: 1px solid #444;
                border-radius: 8px;
                padding: 10px;
                min-width: 220px;
                font-size: 16px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #444;
                border-left-style: solid;
            }
        """)
        
        self.layout.addWidget(select)
        self.layout.addSpacing(20)
        
        # Add animation when selection changes
        select.currentIndexChanged.connect(lambda: self.animate_selection(select))
        
        return select
    
    def animate_checkbox(self, checkbox):
        """Animate checkbox when clicked"""
        animation = QPropertyAnimation(checkbox, b"geometry")
        animation.setDuration(150)
        current_rect = checkbox.geometry()
        
        # Pulse animation
        animation.setKeyValueAt(0, current_rect)
        
        # Slightly larger
        larger_rect = QRect(current_rect.x() - 3, 
                            current_rect.y() - 3,
                            current_rect.width() + 6, 
                            current_rect.height() + 6)
        animation.setKeyValueAt(0.5, larger_rect)
        
        # Back to original size
        animation.setKeyValueAt(1, current_rect)
        
        animation.start()
    
    def animate_slider_change(self, value, label, slider):
        """Animate value label when slider changes"""
        # Update the label text
        label.setText(f"{value}%")
        
        # Create an animation for the handle
        handle_anim = QPropertyAnimation(slider, b"styleSheet")
        handle_anim.setDuration(100)
        
        # Get current stylesheet and add a glow effect
        base_style = """
            QSlider::groove:horizontal {
                border: 1px solid #444;
                height: 12px;
                background: #2A2F3C;
                margin: 2px 0;
                border-radius: 6px;
            }
            QSlider::handle:horizontal {
                background: #8B5CF6;
                border: 1px solid #8B5CF6;
                width: 26px;
                margin: -5px 0;
                border-radius: 13px;
            }
        """
        
        glow_style = """
            QSlider::groove:horizontal {
                border: 1px solid #444;
                height: 12px;
                background: #2A2F3C;
                margin: 2px 0;
                border-radius: 6px;
            }
            QSlider::handle:horizontal {
                background: #9B6DFF;
                border: 1px solid #9B6DFF;
                width: 30px;
                margin: -6px 0;
                border-radius: 15px;
                box-shadow: 0 0 8px #8B5CF6;
            }
        """
        
        handle_anim.setKeyValueAt(0, base_style)
        handle_anim.setKeyValueAt(0.5, glow_style)
        handle_anim.setKeyValueAt(1, base_style)
        handle_anim.start()
        
        # Animate the label
        label_anim = QPropertyAnimation(label, b"font")
        font = label.font()
        original_size = font.pointSize()
        
        font_large = QFont(font)
        font_large.setPointSize(original_size + 2)
        
        label_anim.setDuration(200)
        label_anim.setKeyValueAt(0, font)
        label_anim.setKeyValueAt(0.5, font_large)
        label_anim.setKeyValueAt(1, font)
        label_anim.start()
    
    def animate_selection(self, combobox):
        """Animate combobox when selection changes"""
        animation = QPropertyAnimation(combobox, b"geometry")
        animation.setDuration(200)
        current_rect = combobox.geometry()
        
        # Pulse animation
        animation.setKeyValueAt(0, current_rect)
        
        # Slightly highlight
        highlight_rect = QRect(current_rect.x(), 
                              current_rect.y() - 2,
                              current_rect.width(), 
                              current_rect.height() + 4)
        animation.setKeyValueAt(0.5, highlight_rect)
        
        # Back to original size
        animation.setKeyValueAt(1, current_rect)
        
        animation.start()
        
        # Also change style briefly
        style_anim = QPropertyAnimation(combobox, b"styleSheet")
        style_anim.setDuration(300)
        
        base_style = combobox.styleSheet()
        highlight_style = """
            QComboBox {
                background-color: #352F45;
                color: white;
                border: 1px solid #8B5CF6;
                border-radius: 8px;
                padding: 10px;
                min-width: 220px;
                font-size: 16px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: #8B5CF6;
                border-left-style: solid;
            }
        """
        
        style_anim.setKeyValueAt(0, base_style)
        style_anim.setKeyValueAt(0.3, highlight_style)
        style_anim.setKeyValueAt(1, base_style)
        
        style_anim.start()


class SettingsView(BaseView):
    """View for application settings"""
    
    def __init__(self, parent=None):
        # Initialize cards list before calling super().__init__
        # This ensures it exists when setup_ui is called
        self.cards = []
        super().__init__(parent)
        
    def setup_ui(self):
        """Set up the UI components"""
        super().setup_ui()
        
        # Main title with larger font for 1600x800 resolution
        title_label = QLabel("Settings")
        title_label.setStyleSheet("font-size: 38px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Customize your GAMINATOR experience")
        subtitle_label.setStyleSheet("font-size: 22px; color: #aaadb0; margin-bottom: 30px;")
        self.main_layout.addWidget(subtitle_label)
        
        # Settings layout with two columns
        settings_layout = QHBoxLayout()
        settings_layout.setSpacing(40)  # Increased spacing between columns
        
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
        
        # Store cards for animations
        self.cards.append(voice_settings)
        self.cards.append(system_settings)
        
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
        
        # Store cards for animations
        self.cards.append(gesture_settings)
        self.cards.append(notification_settings)
        
        # Add columns to settings layout with proportional sizes
        settings_layout.addLayout(left_layout, 1)
        settings_layout.addLayout(right_layout, 1)
        
        # Add settings layout to main layout
        self.main_layout.addLayout(settings_layout)
        self.main_layout.addStretch()
        
        # Add navigation bar at the bottom
        self.main_layout.addLayout(self.nav_layout)
        
        # Set up entry animations for cards
        self.animate_cards_entry()
    
    def animate_cards_entry(self):
        """Create staggered entry animations for the settings cards"""
        for i, card in enumerate(self.cards):
            # Start with zero opacity
            card.setGraphicsEffect(None)  # Clear any existing effects
            
            # Create the animation with a staggered delay
            anim = QPropertyAnimation(card, b"pos")
            anim.setDuration(600)
            anim.setStartValue(card.pos() + QPoint(0, 50))  # Start 50 pixels below
            anim.setEndValue(card.pos())
            anim.setEasingCurve(QEasingCurve.OutCubic)
            
            # Delay each card slightly
            anim.setStartTime(i * 150)
            anim.start()

