from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, radius=PLAYER_RADIUS)
    self.x = x
    self.y = y
    self.rotation = 0
    self.timer = 0
    # in the player class

  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
  
  def draw(self, screen):
     return pygame.draw.polygon(screen, "white", self.triangle(), 2)
  
  def rotate(self, dt):
     self.rotation += PLAYER_TURN_SPEED * dt


  def update(self, dt):
      if self.timer > 0:
         self.timer -= dt
      if self.timer < 0:
         self.timer = 0
      keys = pygame.key.get_pressed()

      if keys[pygame.K_a]:
         self.rotate(-dt)
                     
      if keys[pygame.K_d]:
         self.rotate(dt)

      if keys[pygame.K_w]:
         self.move(dt)

      if keys[pygame.K_s]:
         self.move(-dt)

      if keys[pygame.K_SPACE]:
         self.shoot()
         self.timer = PLAYER_SHOOT_COOLDOWN


  def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
     if self.timer > 0:
        return
     new_shot = Shot(*self.position)
     new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
