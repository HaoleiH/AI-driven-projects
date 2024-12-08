import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
T.REX_WIDTH, T.REX_HEIGHT = 50, 50
JUMP_VEL = 15
GRAVITY = 1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (165, 42, 42)

# T-Rex properties
trex_x, trex_y = 100, HEIGHT - T.REX_HEIGHT - 20
trex_vy = 0
is_jumping = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                trex_vy = -JUMP_VEL

    # Move T-Rex
    if is_jumping:
        trex_y += trex_vy
        trex_vy += GRAVITY
        if trex_y >= HEIGHT - T.REX_HEIGHT - 20:
            trex_y = HEIGHT - T.REX_HEIGHT - 20
            is_jumping = False

    # Draw everything
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GROUND_BROWN, (0, HEIGHT - 20, WIDTH, 20))
    pygame.draw.rect(screen, (0, 0, 0), (trex_x, trex_y, T.REX_WIDTH, T.REX_HEIGHT))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)