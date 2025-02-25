import pygame
from player import *
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize all of pygame
    pygame.init()

    #Create a clock object to manage the frame time
    clock = pygame.time.Clock()
    dt = 0      #delta time aka track the time between frames

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Fixed typo
    pygame.display.set_caption("Asteroids")


    #Set to spawn player in middle of screen
    center_x = SCREEN_WIDTH/2
    center_y = SCREEN_HEIGHT/2

    player_instance = Player(center_x, center_y)

    #create groups updatable and drawable
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #add Player object to updatable and drawable
    updatable.add(player_instance)
    drawable.add(player_instance)

    # Main game loop
    while True:  # Infinite loop for the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Allow user to close the window
                pygame.quit()
                return
            
        updatable.update(dt)

        # Fill the screen with black
        screen.fill((0, 0, 0))



        #using groups to draw
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        #cap frame rate to 60 and calculate dt
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
