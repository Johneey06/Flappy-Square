import pygame
import random

class Projectile:
    def __init__(self):
    # Initialize projectile attributes
        self.projectile_width = 30
        self.projectile_height = 30
        self.projectile_velocity = 300
        self.projectiles = []

    def generate_projectiles(self, screen_height, screen_width):
        y_position = random.randint(0, screen_height - self.projectile_height)

        projectile = pygame.Rect(screen_width, y_position, self.projectile_width, self.projectile_height)

        self.projectiles.append(projectile)

    def draw_projectiles(self, screen):
        for projectile in self.projectiles:
            pygame.draw.rect(screen, (255, 0, 0), projectile)

    def update_projectiles(self, dt):
        for projectile in self.projectiles:
            projectile.x -= self.projectile_velocity * dt
        
        # Remove off-screen projectiles

        self.projectiles = [projectile for projectile in self.projectiles if projectile.x > - self.projectile_width]