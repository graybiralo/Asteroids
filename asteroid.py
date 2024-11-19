import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y,radius)
        self.velocity = velocity

        for container in self.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity_1)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity_2)
        

        for container in self.containers:
            container.add(new_asteroid_1)
            container.add(new_asteroid_2)