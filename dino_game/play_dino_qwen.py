import time
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()#(executable_path='path/to/chromedriver')
driver.get('chrome://dino')

# Wait for the game to load
time.sleep(2)

# Start the game
driver.execute_script("Runner.instance_.restart()")

# Capture the game screen
def capture_screen():
    canvas = driver.find_element_by_tag_name('canvas')
    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    image = np.frombuffer(canvas_base64.decode('base64'), np.uint8)
    return cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

# Detect obstacles
def detect_obstacles(screen):
    # Define a region of interest where obstacles appear
    roi = screen[200:300, 200:400]
    # Apply a threshold to detect obstacles
    _, threshold = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
    # Count the number of white pixels (obstacles)
    obstacle_count = cv2.countNonZero(threshold)
    return obstacle_count > 500

# Main game loop
while True:
    screen = capture_screen()
    if detect_obstacles(screen):
        driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    time.sleep(0.05)

# Close the browser
driver.quit()