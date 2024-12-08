import pyautogui
import time
from PIL import ImageGrab, ImageOps

# Coordinates for the game (adjust based on your screen setup)
# You may need to update these values based on your screen resolution
GAME_REGION = (580, 179, 756, 237)  # (left, top, width, height)
OBSTACLE_REGION = (660, 265, 35, 82)  # (x_offset, y_offset, width, height)

def detect_obstacle():
    """
    Detect obstacles in the obstacle region using pixel intensity.
    Returns True if an obstacle is detected.
    """
    # Take a screenshot of the obstacle region
    image = ImageGrab.grab(bbox=OBSTACLE_REGION)
    gray_image = ImageOps.grayscale(image)
    pixel_sum = sum(gray_image.getdata())
    
    # Set a threshold for detecting obstacles
    return pixel_sum < 10000

def jump():
    """Simulate a jump by pressing the spacebar."""
    pyautogui.press("space")

def main():
    print("Starting Dino bot... Get ready!")
    time.sleep(3)  # Wait for user to switch to the game
    
    while True:
        if detect_obstacle():
            jump()
        time.sleep(0.05)  # Small delay to avoid excessive CPU usage

if __name__ == "__main__":
    main()
