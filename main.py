import pygame
import sys

# Initialize Pygame
pygame.init()
print("noa is the best !!!!")

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Background")

# Load background image
background = pygame.image.load('background_image.jpg')
background_rect = background.get_rect()

# Initial position of the background
background_x = 0

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update background position
    background_x -= 1  # Move background to the left

    # Wrap background around when it goes off-screen
    if background_x <= -background_rect.width:
        background_x = 0

    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Blit the background onto the screen
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + background_rect.width, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
