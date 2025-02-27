import sys
import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Game initialization
    print("Starting Asteroids!")

    pygame.init()
    
    # Screen setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Timing
    clock = pygame.time.Clock()
    dt = 0  # Delta time: track time between frames

    # Sprite groups
    updatable = pygame.sprite.Group()  # Objects to be updated
    drawable = pygame.sprite.Group()   # Objects to be drawn
    asteroids = pygame.sprite.Group()  # Specific group for asteroids
    shots = pygame.sprite.Group()      #Specific group for shots

    # Link Player to sprite groups
    Player.containers = (updatable, drawable)

    # Link Asteroid to sprite groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Link AsteroidField to updatable group
    AsteroidField.containers = (updatable)

    #Link Shot to sprite groups
    Shot.containers = (updatable,drawable,shots)

    # Create initial game objects
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Center the player
    asteroid_field_instance = AsteroidField()  # Spawn initial asteroid field

    # Main game loop
    
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects
        updatable.update(dt)

        for Asteroid_unit in asteroids:
            if player_instance.collides_with(Asteroid_unit):
                print ("Game over!")
                sys.exit()

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen (black background)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Refresh the display

        # Cap frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
