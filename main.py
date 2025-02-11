import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot


def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  player= Player(x = SCREEN_WIDTH / 2, y =  SCREEN_HEIGHT /2)
  asteroid_field_gen = AsteroidField()



  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(000000)
    dt = (clock.tick(60)/1000)
    updatable.update(dt)

    for obj in drawable:
        obj.draw(screen) 

    for asteroid in asteroids:
      if player.collision_check(asteroid):
        print("Game over!")
        exit()

    for asteroid in asteroids:
      for shot in shots:
        if shot.collision_check(asteroid):
          asteroid.split()
          shot.kill() 

    
    pygame.display.flip()
    

  

if __name__ == "__main__":
  main()