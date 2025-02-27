import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
  containers = None

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)


  def draw(self, screen):
    pygame.draw.circle(screen,"white", self.position, self.radius)
  

  def move(self, delta):
      self.position += delta

  def update(self, dt):
    self.move(self.velocity * dt)