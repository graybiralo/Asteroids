import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
from circleshape import CircleShape
import select
from pip._vendor.pyparsing.core import Forward

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
            if self.timer <= 0:
            # Create a new shot at the player's current position
                new_shot = Shot(self.position.x, self.position.y)
            # Set the shot's velocity in the direction the player is facing
                direction = pygame.Vector2(0, 1).rotate(self.rotation)
                new_shot.velocity = direction * PLAYER_SHOOT_SPEED
                self.timer = PLAYER_SHOOT_COOLDOWN
                return new_shot
            
    def update(self, dt, shots_group):
        if self.timer > 0:
            self.timer -= dt
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
            shot = self.shoot()
            if shot:
                shots_group.add(shot)        

    

    # in the player class
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


