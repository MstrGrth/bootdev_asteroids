import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (80, 80, 80), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_velo = random.uniform(20, 50)
            asteroid_split_one = self.velocity.rotate(random_velo)
            asteroid_split_two = self.velocity.rotate(-random_velo)
            asteroid_new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_speed_one = asteroid_split_one * 1.2
            asteroid_speed_two = asteroid_split_two * 1.2
            asteroid_one_new = Asteroid(self.position.x, self.position.y, asteroid_new_radius, asteroid_speed_one)
            asteroid_two_new = Asteroid(self.position.x, self.position.y, asteroid_new_radius, asteroid_speed_two)
            return asteroid_one_new, asteroid_two_new




