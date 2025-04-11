import pygame

class Square:
    def __init__(self):
         # Initialize square attributes
        self.square_width = 30
        self.square_height = 30
        self.square_x = 100
        self.square_y = 300
        self.square_velocity = 0

        self.gravity = 1200
        self.jump_strength = -300

        self.square = pygame.Rect(self.square_x, self.square_y, self.square_width, self.square_height)

        self.is_jumping = False
    
    def update_square(self, dt):
        self.square_velocity += self.gravity * dt
        self.square.y += self.square_velocity * dt

    
    def draw_square(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.square)

    def handle_jump(self):
        self.square_velocity = self.jump_strength 
