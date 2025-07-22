import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroidfields = AsteroidField()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over")
                sys.exit()
            for bullet in shots:
                if asteroid.collisions(bullet):
                    bullet.kill()
                    split_result = asteroid.split()
                    if split_result is not None:
                        new_rock_1, new_rock_2 = split_result
                        asteroids.add(new_rock_1)
                        asteroids.add(new_rock_2)



        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
