import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 200

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game settings
GRAVITY = 1
JUMP_STRENGTH = -15
SPEED = 5

# Load images
dino_images = [pygame.image.load("dino1.png"), pygame.image.load("dino2.png")]
cactus_image = pygame.image.load("cactus.png")

# Resize images
dino_images = [pygame.transform.scale(img, (40, 40)) for img in dino_images]
cactus_image = pygame.transform.scale(cactus_image, (30, 40))

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Dino class
class Dino:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT - 50
        self.velocity = 0
        self.image_index = 0
        self.image = dino_images[self.image_index]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity = JUMP_STRENGTH
            self.is_jumping = True

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y > SCREEN_HEIGHT - 50:
            self.y = SCREEN_HEIGHT - 50
            self.velocity = 0
            self.is_jumping = False

        self.image_index = (self.image_index + 1) % len(dino_images)
        self.image = dino_images[self.image_index]
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Cactus class
class Cactus:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - 40
        self.image = cactus_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.x -= SPEED
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Game loop
def game_loop():
    dino = Dino()
    cacti = []
    score = 0
    font = pygame.font.Font(None, 36)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        # Add new cactus
        if len(cacti) == 0 or cacti[-1].x < SCREEN_WIDTH - 150:
            cacti.append(Cactus())

        # Update dino and cacti
        dino.update()
        for cactus in cacti:
            cactus.update()

        # Check for collisions
        for cactus in cacti:
            if dino.rect.colliderect(cactus.rect):
                running = False

        # Remove off-screen cacti and update score
        cacti = [cactus for cactus in cacti if cactus.x > -30]
        score += len(cacti)

        # Draw everything
        screen.fill(WHITE)
        dino.draw(screen)
        for cactus in cacti:
            cactus.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

# Run the game
game_loop()