import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize all of pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Fixed typo
    pygame.display.set_caption("My Pygame Window")

    # Main game loop
    while True:  # Infinite loop for the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow user to close the window
                pygame.quit()
                return
        
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
