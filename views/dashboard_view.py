
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
                            QProgressBar, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen
from views.base_view import BaseView

class DashboardView(BaseView):
    """View for the dashboard and statistics"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def setup_ui(self):
        """Set up the UI components"""
        super().setup_ui()
        
        # Main title
        title_label = QLabel("Dashboard")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Monitor your usage statistics and activity")
        subtitle_label.setStyleSheet("font-size: 14px; color: #888;")
        self.main_layout.addWidget(subtitle_label)
        
        # Stats overview section
        stats_layout = QHBoxLayout()
        
        # Voice command stats
        voice_stats = self.create_stat_widget(
            "Voice Commands", 
            "142", 
            "75% success rate",
            "#8B5CF6"
        )
        
        # Gesture control stats
        gesture_stats = self.create_stat_widget(
            "Gestures Used", 
            "96", 
            "68% success rate",
            "#22C55E"
        )
        
        # Session stats
        session_stats = self.create_stat_widget(
            "Sessions", 
            "24", 
            "42 minutes avg",
            "#3B82F6"
        )
        
        stats_layout.addWidget(voice_stats)
        stats_layout.addWidget(gesture_stats)
        stats_layout.addWidget(session_stats)
        
        self.main_layout.addLayout(stats_layout)
        
        # Usage graphs section
        graphs_layout = QVBoxLayout()
        
        # Daily usage chart
        daily_chart = QWidget()
        daily_layout = QVBoxLayout(daily_chart)
        
        daily_title = QLabel("Daily Usage")
        daily_title.setStyleSheet("font-weight: bold;")
        daily_layout.addWidget(daily_title)
        
        # Placeholder for chart - in a real app, this would be a proper chart widget
        chart_placeholder = QWidget()
        chart_placeholder.setMinimumHeight(150)
        chart_placeholder.setStyleSheet("background-color: #1E212A; border-radius: 5px;")
        daily_layout.addWidget(chart_placeholder)
        
        daily_chart.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 15px;")
        graphs_layout.addWidget(daily_chart)
        
        # Recent activities
        activities = QWidget()
        activities_layout = QVBoxLayout(activities)
        
        activities_title = QLabel("Recent Activities")
        activities_title.setStyleSheet("font-weight: bold;")
        activities_layout.addWidget(activities_title)
        
        # Activity 1
        act1 = QHBoxLayout()
        act1_time = QLabel("10:35 AM")
        act1_time.setStyleSheet("color: #888;")
        act1_desc = QLabel("Browser opened via voice command")
        act1.addWidget(act1_time)
        act1.addWidget(act1_desc)
        act1.addStretch()
        activities_layout.addLayout(act1)
        
        # Separator line
        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        line1.setStyleSheet("background-color: #444;")
        activities_layout.addWidget(line1)
        
        # Activity 2
        act2 = QHBoxLayout()
        act2_time = QLabel("10:28 AM")
        act2_time.setStyleSheet("color: #888;")
        act2_desc = QLabel("Volume increased via gesture")
        act2.addWidget(act2_time)
        act2.addWidget(act2_desc)
        act2.addStretch()
        activities_layout.addLayout(act2)
        
        # Separator line
        line2 = QFrame()
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)
        line2.setStyleSheet("background-color: #444;")
        activities_layout.addWidget(line2)
        
        # Activity 3
        act3 = QHBoxLayout()
        act3_time = QLabel("10:15 AM")
        act3_time.setStyleSheet("color: #888;")
        act3_desc = QLabel("Scroll down gesture detected")
        act3.addWidget(act3_time)
        act3.addWidget(act3_desc)
        act3.addStretch()
        activities_layout.addLayout(act3)
        
        activities.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 15px;")
        graphs_layout.addWidget(activities)
        
        self.main_layout.addLayout(graphs_layout)
        
        self.main_layout.addStretch()
        
        # Add navigation bar at the bottom
        self.main_layout.addLayout(self.nav_layout)
    
    def create_stat_widget(self, title, value, subtitle, color):
        """Create a statistics widget with the given data"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #888;")
        layout.addWidget(title_label)
        
        # Value
        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 28px; font-weight: bold; color: {color};")
        layout.addWidget(value_label)
        
        # Progress bar
        progress = QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(75 if "75%" in subtitle else 68 if "68%" in subtitle else 80)
        progress.setTextVisible(False)
        progress.setStyleSheet(f"""
            QProgressBar {{
                background-color: #1E212A;
                border-radius: 3px;
                height: 6px;
            }}
            QProgressBar::chunk {{
                background-color: {color};
                border-radius: 3px;
            }}
        """)
        layout.addWidget(progress)
        
        # Subtitle
        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet("color: #888; font-size: 12px;")
        layout.addWidget(sub_label)
        
        widget.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 15px;")
        return widget
