import cv2
import autoit
import time
import numpy as np
from PIL import ImageGrab
import keyboard

# Template reinladen
template = cv2.imread("button_template.png", cv2.IMREAD_UNCHANGED)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

running = False

def find_button_on_screen():
    # Button suchen indem mit Screenshot abgeglichen wird
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Schwellenwert
    threshold = 0.5
    if max_val >= threshold:
        return max_loc
    return None

def click_button(x, y):
    center_x = x + w // 2
    center_y = y + h // 2
    print(f"Button bei: ({center_x}, {center_y})")
    autoit.mouse_move(center_x, center_y, speed=3)
    autoit.mouse_click("left", center_x, center_y)

def toggle_running():
    global running
    running = not running
    print(f"Running: {running}")

keyboard.add_hotkey('F8', toggle_running)

# Hauptschleife
while True:
    if running:
        # Alle 0.5 Sekunden einen Screenshot machen und nach dem Button suchen
        button_location = find_button_on_screen()
        if button_location:
            print(f"Button gefunden bei: {button_location}")
            # wenn er gefunden wurde wird er geklickt
            click_button(*button_location)
        else:
            print("Button nicht gefunden.")
    time.sleep(0.5)