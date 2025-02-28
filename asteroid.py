import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  containers = None

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)


  def draw(self, screen):
    pygame.draw.circle(screen,"white", self.position, self.radius, 2)
  
  def split(self):
      #Remove current Asteroid
      self.kill()
      
      #if asteroid is too small, don't split
      if self.radius <= ASTEROID_MIN_RADIUS:
        return
      
      #random angle for split
      random_angle = random.uniform(20, 50)


      # Calculate the new velocities for the split asteroids
      first_asteroid_velocity = self.velocity.rotate(random_angle)
      second_asteroid_velocity = self.velocity.rotate(-random_angle)

      #new radius for split
      new_radius = self.radius - ASTEROID_MIN_RADIUS


      #Create first split asteroid
      first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
      first_asteroid.velocity = first_asteroid_velocity * 1.2

      #Create second split asteroid
      second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
      second_asteroid.velocity = second_asteroid_velocity * 1.2



  def update(self, dt):
    self.position += self.velocity * dt