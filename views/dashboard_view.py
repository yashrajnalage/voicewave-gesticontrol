
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout, QHBoxLayout, 
                           QGridLayout, QFrame, QTabWidget, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from views.base_view import BaseView
from views.voice_command_view import CommandHistory

class StatCard(QFrame):
    """Statistics card for the dashboard"""
    
    def __init__(self, title, value, description, trend, trend_value, icon, parent=None):
        super().__init__(parent)
        self.title = title
        self.value = value
        self.description = description
        self.trend = trend  # "up", "down", or "neutral"
        self.trend_value = trend_value
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
        """)
        
        layout = QHBoxLayout()
        
        # Left side - icon
        icon_label = QLabel(self.icon)
        icon_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(icon_label)
        
        # Right side - info
        info_layout = QVBoxLayout()
        
        # Title
        title_label = QLabel(self.title)
        title_label.setStyleSheet("color: #B0B0B0; font-size: 9pt;")
        
        # Value
        value_label = QLabel(str(self.value))
        value_label.setFont(QFont("Arial", 18, QFont.Bold))
        
        # Description and trend
        desc_layout = QHBoxLayout()
        desc_label = QLabel(self.description)
        desc_label.setStyleSheet("color: #B0B0B0; font-size: 8pt;")
        
        trend_icon = "↑" if self.trend == "up" else "↓" if self.trend == "down" else "→"
        trend_color = "#10B981" if self.trend == "up" else "#EF4444" if self.trend == "down" else "#B0B0B0"
        
        trend_label = QLabel(f"{trend_icon} {self.trend_value}")
        trend_label.setStyleSheet(f"color: {trend_color}; font-size: 8pt;")
        
        desc_layout.addWidget(desc_label)
        desc_layout.addWidget(trend_label)
        desc_layout.addStretch()
        
        info_layout.addWidget(title_label)
        info_layout.addWidget(value_label)
        info_layout.addLayout(desc_layout)
        
        layout.addLayout(info_layout)
        layout.addStretch()
        
        self.setLayout(layout)


class DashboardView(BaseView):
    """Dashboard view for the application"""
    
    def __init__(self, parent=None):
        self.all_commands = [
            {"id": "1", "type": "voice", "command": "Open Browser", "timestamp": "10:15 AM", "status": "success"},
            {"id": "2", "type": "gesture", "command": "Swipe Left", "timestamp": "10:20 AM", "status": "success"},
            {"id": "3", "type": "voice", "command": "Volume Up", "timestamp": "10:12 AM", "status": "success"},
            {"id": "4", "type": "gesture", "command": "Pinch Zoom", "timestamp": "10:18 AM", "status": "success"},
            {"id": "5", "type": "voice", "command": "Launch Spotify", "timestamp": "10:10 AM", "status": "error"},
            {"id": "6", "type": "gesture", "command": "Scroll Down", "timestamp": "10:15 AM", "status": "error"},
            {"id": "7", "type": "voice", "command": "Next Slide", "timestamp": "10:05 AM", "status": "success"},
            {"id": "8", "type": "gesture", "command": "Click", "timestamp": "10:14 AM", "status": "success"},
        ]
        self.voice_commands = [cmd for cmd in self.all_commands if cmd["type"] == "voice"]
        self.gesture_commands = [cmd for cmd in self.all_commands if cmd["type"] == "gesture"]
        super().__init__(parent)
        
    def setup_ui(self):
        super().setup_ui()
        
        # Title
        title_label = QLabel("Dashboard")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.main_layout.addWidget(title_label)
        
        subtitle = QLabel("Monitor your control activity and performance")
        subtitle.setStyleSheet("color: #B0B0B0;")
        self.main_layout.addWidget(subtitle)
        
        # Stats grid
        stats_layout = QGridLayout()
        
        voice_card = StatCard("Voice Commands", 24, "Used today", "up", "12%", "🎤")
        gesture_card = StatCard("Gesture Controls", 18, "Used today", "up", "8%", "👋")
        recognition_card = StatCard("Recognition Rate", "92%", "Accuracy", "neutral", "0%", "⚡")
        time_card = StatCard("Active Time", "3h 24m", "Today", "down", "5%", "⏱️")
        
        stats_layout.addWidget(voice_card, 0, 0)
        stats_layout.addWidget(gesture_card, 0, 1)
        stats_layout.addWidget(recognition_card, 0, 2)
        stats_layout.addWidget(time_card, 0, 3)
        
        self.main_layout.addLayout(stats_layout)
        
        # Main content grid (activity history and popular commands)
        content_layout = QGridLayout()
        
        # Activity history card
        activity_frame = QFrame()
        activity_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
            QTabWidget::pane {
                border: none;
                background-color: transparent;
            }
            QTabBar::tab {
                background-color: #1A1F2C;
                color: #B0B0B0;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                padding: 8px 12px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #8B5CF6;
                color: white;
            }
        """)
        
        activity_layout = QVBoxLayout(activity_frame)
        
        # Header
        activity_header = QHBoxLayout()
        activity_icon = QLabel("📊")
        activity_title = QLabel("Activity History")
        activity_title.setFont(QFont("Arial", 14, QFont.Bold))
        
        activity_header.addWidget(activity_icon)
        activity_header.addWidget(activity_title)
        activity_header.addStretch()
        
        activity_layout.addLayout(activity_header)
        
        # Tab widget for different command types
        tabs = QTabWidget()
        
        # All commands tab
        all_tab = QWidget()
        all_layout = QVBoxLayout(all_tab)
        all_layout.setContentsMargins(0, 10, 0, 0)
        all_history = CommandHistory(self.all_commands)
        all_layout.addWidget(all_history)
        
        # Voice commands tab
        voice_tab = QWidget()
        voice_layout = QVBoxLayout(voice_tab)
        voice_layout.setContentsMargins(0, 10, 0, 0)
        voice_history = CommandHistory(self.voice_commands)
        voice_layout.addWidget(voice_history)
        
        # Gesture commands tab
        gesture_tab = QWidget()
        gesture_layout = QVBoxLayout(gesture_tab)
        gesture_layout.setContentsMargins(0, 10, 0, 0)
        gesture_history = CommandHistory(self.gesture_commands)
        gesture_layout.addWidget(gesture_history)
        
        tabs.addTab(all_tab, "All Commands")
        tabs.addTab(voice_tab, "Voice Only")
        tabs.addTab(gesture_tab, "Gestures Only")
        
        activity_layout.addWidget(tabs)
        
        # Popular commands card
        popular_frame = QFrame()
        popular_frame.setStyleSheet("""
            QFrame {
                background-color: #2A2F3C;
                border-radius: 10px;
                border: 1px solid #3A3F4C;
            }
        """)
        
        popular_layout = QVBoxLayout(popular_frame)
        
        # Header
        popular_header = QHBoxLayout()
        popular_icon = QLabel("⌨️")
        popular_title = QLabel("Popular Commands")
        popular_title.setFont(QFont("Arial", 14, QFont.Bold))
        
        popular_header.addWidget(popular_icon)
        popular_header.addWidget(popular_title)
        popular_header.addStretch()
        
        popular_layout.addLayout(popular_header)
        
        # Voice commands section
        voice_section = QFrame()
        voice_section.setStyleSheet("""
            QFrame {
                background-color: rgba(139, 92, 246, 0.1);
                border-radius: 5px;
            }
        """)
        
        vs_layout = QVBoxLayout(voice_section)
        
        vs_title = QLabel("Voice Commands")
        vs_title.setFont(QFont("Arial", 10, QFont.Bold))
        vs_layout.addWidget(vs_title)
        
        # Voice command list
        vs_commands = [
            ("Open Browser", "28 times"),
            ("Volume Up", "24 times"),
            ("Close Window", "19 times")
        ]
        
        for cmd, count in vs_commands:
            cmd_layout = QHBoxLayout()
            cmd_name = QLabel(cmd)
            cmd_name.setStyleSheet("color: #B0B0B0;")
            
            cmd_count = QLabel(count)
            cmd_count.setStyleSheet("""
                background-color: rgba(139, 92, 246, 0.2);
                color: #8B5CF6;
                border-radius: 10px;
                padding: 2px 6px;
                font-size: 8pt;
            """)
            
            cmd_layout.addWidget(cmd_name)
            cmd_layout.addStretch()
            cmd_layout.addWidget(cmd_count)
            
            vs_layout.addLayout(cmd_layout)
        
        popular_layout.addWidget(voice_section)
        
        # Gesture commands section
        gesture_section = QFrame()
        gesture_section.setStyleSheet("""
            QFrame {
                background-color: rgba(139, 92, 246, 0.1);
                border-radius: 5px;
            }
        """)
        
        gs_layout = QVBoxLayout(gesture_section)
        
        gs_title = QLabel("Gesture Controls")
        gs_title.setFont(QFont("Arial", 10, QFont.Bold))
        gs_layout.addWidget(gs_title)
        
        # Gesture command list
        gs_commands = [
            ("Swipe Left", "32 times"),
            ("Click", "26 times"),
            ("Scroll Down", "15 times")
        ]
        
        for cmd, count in gs_commands:
            cmd_layout = QHBoxLayout()
            cmd_name = QLabel(cmd)
            cmd_name.setStyleSheet("color: #B0B0B0;")
            
            cmd_count = QLabel(count)
            cmd_count.setStyleSheet("""
                background-color: rgba(139, 92, 246, 0.2);
                color: #8B5CF6;
                border-radius: 10px;
                padding: 2px 6px;
                font-size: 8pt;
            """)
            
            cmd_layout.addWidget(cmd_name)
            cmd_layout.addStretch()
            cmd_layout.addWidget(cmd_count)
            
            gs_layout.addLayout(cmd_layout)
        
        popular_layout.addWidget(gesture_section)
        
        # Add to content layout
        content_layout.addWidget(activity_frame, 0, 0, 1, 3)
        content_layout.addWidget(popular_frame, 0, 3)
        
        content_layout.setColumnStretch(0, 3)
        content_layout.setColumnStretch(3, 1)
        
        self.main_layout.addLayout(content_layout)
