import pyautogui
import time
import cv2
import numpy as np

# Region of the screen to capture (adjust based on Dino's position)
# You might need to tweak these coordinates based on your screen setup
GAME_REGION = (580, 160, 756, 200)  # (x, y, width, height)

def press_jump():
    """Simulate the space bar press to make the Dino jump."""
    pyautogui.press('space')

def is_obstacle_present(screen):
    """Detect obstacles in the game region for dark mode."""
    # Convert to grayscale for simpler processing
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image since obstacles are bright on a dark background
    inverted = cv2.bitwise_not(gray)
    # Apply a binary threshold to highlight obstacles
    _, thresholded = cv2.threshold(inverted, 200, 255, cv2.THRESH_BINARY)
    # Define a region of interest where obstacles appear
    roi = thresholded[115:167, 60:100]  # Focus on the area in front of the Dino
    # Count non-zero pixels to detect obstacles
    pixel_sum = np.sum(roi)                    
    # If pixel_sum exceeds a certain value, an obstacle is detected
    cv2.imshow('ROI', roi)  # Show the region of interest
    #cv2.imshow('Thresholded', thresholded)  # Show the thresholded image
    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        cv2.destroyAllWindows()
        exit()

    return pixel_sum > 2080*255*0.95  # Adjust based on testing

def main():
    print("Starting the Dino automation in dark mode...")
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
