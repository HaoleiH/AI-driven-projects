import pyautogui
import time
import cv2
import numpy as np

# Region of the screen to capture (adjust based on Dino's position)
# You might need to tweak these coordinates based on your screen setup
GAME_REGION = (580, 179, 756, 237)  # (x, y, width, height)

def press_jump():
    """Simulate the space bar press to make the Dino jump."""
    pyautogui.press('space')

def is_obstacle_present(screen):
    """Detect obstacles in the game region."""
    # Convert to grayscale for simpler processing
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # Apply threshold to detect obstacles
    _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    # Sum up the pixels in the thresholded area
    pixel_sum = np.sum(thresholded)
    # If pixel_sum exceeds a certain value, an obstacle is detected
    return pixel_sum > 3000  # Adjust based on testing

def main():
    print("Starting the Dino automation...")
    time.sleep(3)  # Time to switch to the game window
    while True:
        # Take a screenshot of the game region
        screen = pyautogui.screenshot(region=GAME_REGION)
        # Convert to a NumPy array for OpenCV processing
        screen = np.array(screen)
        # Check for obstacles
        if is_obstacle_present(screen):
            press_jump()
        # Small delay to prevent excessive CPU usage
        time.sleep(0.01)

if __name__ == "__main__":
    main()
