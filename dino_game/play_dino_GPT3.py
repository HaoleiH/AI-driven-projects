import cv2
import numpy as np
from PIL import ImageGrab

# Global variables for user-defined areas
game_area = None
obstacle_area = None
selection_start = None
selection_end = None
is_selecting = False

def select_area(event, x, y, flags, param):
    """Mouse callback function for selecting areas."""
    global selection_start, selection_end, is_selecting, game_area, obstacle_area

    if event == cv2.EVENT_LBUTTONDOWN:
        # Start selection
        selection_start = (x, y)
        is_selecting = True

    elif event == cv2.EVENT_MOUSEMOVE and is_selecting:
        # Update selection end as the mouse moves
        selection_end = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        # Finish selection
        selection_end = (x, y)
        is_selecting = False

        # Determine the selected region
        x1, y1 = selection_start
        x2, y2 = selection_end
        selected_area = (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

        # Assign to game_area or obstacle_area based on the current step
        if game_area is None:
            print(f"Game area selected: {selected_area}")
            game_area = selected_area
        elif obstacle_area is None:
            print(f"Obstacle area selected: {selected_area}")
            obstacle_area = selected_area

def draw_red_box(frame, area, label):
    """Draw a labeled red box on the frame."""
    if area:
        x, y, w, h = area
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

def main():
    global game_area, obstacle_area

    print("Select the game area and then the obstacle area. Press 'q' to quit.")
    cv2.namedWindow("Select Areas")
    cv2.setMouseCallback("Select Areas", select_area)

    while True:
        # Take a full-screen screenshot
        screenshot = ImageGrab.grab()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Draw the user selections if available
        if game_area:
            draw_red_box(frame, game_area, "Game Area")
        if obstacle_area:
            draw_red_box(frame, obstacle_area, "Obstacle Area")

        # Show the current selection
        if is_selecting and selection_start and selection_end:
            x1, y1 = selection_start
            x2, y2 = selection_end
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)

        cv2.imshow("Select Areas", frame)

        # Quit the selection process with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

    if game_area and obstacle_area:
        print(f"Game Area: {game_area}")
        print(f"Obstacle Area: {obstacle_area}")
        # Continue with further logic using these areas...

if __name__ == "__main__":
    main()
