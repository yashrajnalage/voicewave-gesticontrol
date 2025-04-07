
# GAMINATOR

GAMINATOR is a desktop application that allows users to control their computer using voice commands and hand gestures, eliminating the need for traditional keyboard and mouse inputs.

## Features

- **Voice Command Control**: Use your voice to control applications, navigate your system, and perform actions
- **Gesture Recognition**: Control your computer with hand gestures captured via your webcam
- **Dashboard**: Monitor your usage statistics and activity history
- **Customizable Settings**: Adjust sensitivity, language, notification preferences and more

## Requirements

- Python 3.7+
- PyQt5
- OpenCV
- SpeechRecognition
- PyAudio
- NumPy

## Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/gaminator.git
cd gaminator
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

Run the main application:
```bash
python gaminator.py
```

## Project Structure

- `gaminator.py` - Main application entry point
- `views/` - UI views for different screens
  - `base_view.py` - Base class for all views
  - `home_view.py` - Home screen
  - `voice_command_view.py` - Voice command interface
  - `gesture_control_view.py` - Gesture control interface
  - `dashboard_view.py` - Statistics and activity dashboard
  - `settings_view.py` - Application settings

## Voice Commands

Example voice commands include:
- "Open Browser"
- "Volume Up/Down"
- "Close Window"
- "Scroll Down"

## Gesture Controls

Example gestures include:
- Swipe left/right - Navigate between applications
- Pinch to zoom - Zoom in/out
- Open palm - Pause/resume

## License

[MIT License](LICENSE)
