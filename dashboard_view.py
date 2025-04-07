
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
                            QProgressBar, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen
from base_view import BaseView

class StatCard(QWidget):
    """Widget for displaying statistics with a colored indicator"""
    def __init__(self, title, value, subtitle, color, progress=75, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(120)
        self.title = title
        self.value = value
        self.subtitle = subtitle
        self.color = QColor(color)
        self.progress = progress
        
        layout = QVBoxLayout(self)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #888;")
        layout.addWidget(title_label)
        
        # Value
        value_label = QLabel(value)
        value_label.setStyleSheet(f"font-size: 28px; font-weight: bold; color: {color};")
        layout.addWidget(value_label)
        
        # Progress bar
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)
        progress_bar.setValue(progress)
        progress_bar.setTextVisible(False)
        progress_bar.setStyleSheet(f"""
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
        layout.addWidget(progress_bar)
        
        # Subtitle
        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet("color: #888; font-size: 12px;")
        layout.addWidget(sub_label)
        
        self.setStyleSheet("background-color: #2A2F3C; border-radius: 10px; padding: 15px;")


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
        voice_stats = StatCard(
            "Voice Commands", 
            "142", 
            "75% success rate",
            "#8B5CF6",
            75
        )
        
        # Gesture control stats
        gesture_stats = StatCard(
            "Gestures Used", 
            "96", 
            "68% success rate",
            "#22C55E",
            68
        )
        
        # Session stats
        session_stats = StatCard(
            "Sessions", 
            "24", 
            "42 minutes avg",
            "#3B82F6",
            80
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
        
        # Chart widget
        chart_widget = QWidget()
        chart_widget.setMinimumHeight(150)
        chart_widget.setStyleSheet("background-color: #1E212A; border-radius: 5px;")
        chart_widget.paintEvent = lambda e: self.paint_chart(chart_widget, e)
        daily_layout.addWidget(chart_widget)
        
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
    
    def paint_chart(self, widget, event):
        """Paint a simple bar chart"""
        painter = QPainter(widget)
        painter.setRenderHint(QPainter.Antialiasing)
        
        width = widget.width()
        height = widget.height()
        
        # Sample data for the chart
        data = [30, 45, 60, 35, 70, 50, 55]
        max_value = max(data)
        
        # Calculate bar width and spacing
        num_bars = len(data)
        bar_width = (width - 20) / num_bars - 10
        
        # Draw axes
        painter.setPen(QPen(QColor(100, 100, 100), 1))
        painter.drawLine(10, height - 20, width - 10, height - 20)  # X-axis
        
        # Draw bars
        for i, value in enumerate(data):
            bar_height = ((value / max_value) * (height - 40))
            x = 15 + i * (bar_width + 10)
            y = height - 20 - bar_height
            
            # Draw bar with gradient
            gradient = QColor(139, 92, 246)
            painter.setBrush(QBrush(gradient))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(int(x), int(y), int(bar_width), int(bar_height), 4, 4)
            
            # Draw day label
            painter.setPen(QColor(150, 150, 150))
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            painter.drawText(int(x), int(height - 5), days[i])
