import cv2
import autoit
import time
import numpy as np
from PIL import ImageGrab
import keyboard

# Load template
template = cv2.imread("button_template.png", cv2.IMREAD_UNCHANGED)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

running = False

def find_button_on_screen():
    # Search for the button by matching with a screenshot
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Threshold
    threshold = 0.5
    if max_val >= threshold:
        return max_loc
    return None

def click_button(x, y):
    center_x = x + w // 2
    center_y = y + h // 2
    print(f"Button at: ({center_x}, {center_y})")
    autoit.mouse_move(center_x, center_y, speed=3)
    autoit.mouse_click("left", center_x, center_y)

def toggle_running():
    global running
    running = not running
    print(f"Running: {running}")

keyboard.add_hotkey('F8', toggle_running)

# Main loop
while True:
    if running:
        # Take a screenshot every 0.5 seconds and search for the button
        button_location = find_button_on_screen()
        if button_location:
            print(f"Button found at: {button_location}")
            # Click the button if found
            click_button(*button_location)
        else:
            print("Button not found.")
    time.sleep(0.5)