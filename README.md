# Auto Clicker for Roblox Game "Fisch"

A simple auto clicker that detects the "shake" button on the screen and automatically clicks it.

## Prerequisites

- Python 3.x
- OpenCV
- AutoIt
- NumPy
- Pillow
- keyboard

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jacobscr/fisch-auto-shake.git
    cd fisch-auto-shake
    ```

2. Install the dependencies:
    ```bash
    pip install opencv-python pyautoit numpy pillow keyboard
    ```

## Usage

1. Make sure the `button_template.png` file is present in the project directory.
2. Run the `auto_clicker.py` script:
    ```bash
    python auto_clicker.py
    ```

The script will search for the button on the screen every 0.5 seconds and click it if found. It also simulates a shaking movement before clicking. Press `F8` to start or stop the script.
