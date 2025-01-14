from constants import *
from circleshape import *
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        angle_1 = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
        angle_2 = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
        radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        A1 = Asteroid(x,y,radius)
        A2 = Asteroid(x,y,radius)
        A1.velocity = angle_1
        A2.velocity = angle_2