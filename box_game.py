import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move Image with Arrow Keys")

# Load the image
image = pygame.image.load('rock.png')

# Get the rect of the loaded image
image_rect = image.get_rect()


new_width = 100
new_height = 100
image = pygame.transform.scale(image, (new_width, new_height))

# Set the initial position of the image
image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Image speed
image_speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update image position based on arrow key input
    if keys[pygame.K_a]:
        print("Moving left")
        image_rect.x -= image_speed
    if keys[pygame.K_d]:
        image_rect.x += image_speed
    if keys[pygame.K_w]:
        image_rect.y -= image_speed
    if keys[pygame.K_s]:
        image_rect.y += image_speed

    # Ensure the image stays within the screen boundaries
    image_rect.x = max(0, min(image_rect.x, SCREEN_WIDTH - new_width))
    image_rect.y = max(0, min(image_rect.y, SCREEN_HEIGHT - new_height))

    # Clear the screen
    screen.fill(BLACK)

    # Draw the image at the updated position
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

# Quit Pygame
pygame.quit()
sys.exit()