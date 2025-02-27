import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):
  containers = None

  def __init__(self, x, y, rotation=0):

    #initializing Player object that inherits from CircleShape
    #x = x-coord of player
    #y = y-coord of player
    #rotation = initial rotation of player (in degrees)
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = rotation


  def triangle(self):

    #Calculate 3 points of the triangle representing the player
    #return the list of vector2 points representing the triangles verticies (lines)


    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)

  def rotate(self, dt):
    self.rotation += (PLAYER_TURN_SPEED * dt)

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt






  def update(self, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)
    if keys[pygame.K_a]:
        self.rotate(-dt)
    if keys[pygame.K_d]:
        self.rotate(dt)
