import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable.add(player)
    drawable.add(player)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


        screen.fill((0, 0, 0))


        for entity in updatable:
            if isinstance(entity, Player):
                entity.update(dt, shots_group)
            else:
                entity.update(dt)

        # check collision player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        # check collision bullets and asteroids
        for shot in shots_group:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    break

        for shot in shots_group:
            shot.update(dt)

        for entity in drawable:
            entity.draw(screen)

        for shot in shots_group:
            shot.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()