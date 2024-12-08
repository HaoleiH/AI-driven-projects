import cv2
import numpy as np
from PIL import ImageGrab

# Coordinates for the game region (adjust these for your screen setup)
GAME_REGION = (580, 179, 756, 237)  # (left, top, width, height)
OBSTACLE_REGION = (660, 265, 35, 82)  # (x_offset, y_offset, width, height)

def draw_red_box_on_obstacle_area():
    print("Displaying the game region with a red box...")
    
    while True:
        # Grab the game region screenshot
        screenshot = ImageGrab.grab(bbox=GAME_REGION)
        frame = np.array(screenshot)

        # Convert from RGB (Pillow) to BGR (OpenCV) format
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Calculate obstacle region within the game frame
        obstacle_x = OBSTACLE_REGION[0] - GAME_REGION[0]
        obstacle_y = OBSTACLE_REGION[1] - GAME_REGION[1]
        obstacle_width = OBSTACLE_REGION[2]
        obstacle_height = OBSTACLE_REGION[3]

        # Draw a red rectangle to highlight the obstacle area
        top_left = (obstacle_x, obstacle_y)
        bottom_right = (obstacle_x + obstacle_width, obstacle_y + obstacle_height)
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

        # Display the frame
        cv2.imshow("Game Region with Red Box", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    draw_red_box_on_obstacle_area()
