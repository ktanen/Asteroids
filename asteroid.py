import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        
        #The shot asteroid always disapepars
        self.kill()
        
        # Small asteroids disappear without spawning new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Medium and large asteroids split into two
        # asteroids that are one size smaller than the original

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_new_direction = self.velocity.rotate(angle)
        second_new_direction = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_smaller_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_smaller_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_smaller_asteroid.velocity = (1.2 * first_new_direction)
        second_smaller_asteroid.velocity = (1.2 * second_new_direction)
        
        
