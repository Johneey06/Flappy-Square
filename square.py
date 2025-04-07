import pygame

class Square:
    def __init__(self):
         # Initialize square attributes
        self.square_width = 30
        self.square_height = 30
        self.square_x = 50
        self.square_y = 300
        self.square_velocity = 0

        self.gravity = 0.5
        self.jump_strength = -5

        self.square = pygame.Rect(self.square_x, self.square_y, self.square_width, self.square_height)
    
    def update_square(self, screen_height):
        self.square_velocity += self.gravity
        self.square.y += self.square_velocity

        # Ground collision
        if self.square.y > screen_height - self.square_height:
            self.square.y = screen_height - self.square_height
        # Ceiling collision
        elif self.square.y < 0:
            self.square.y = 0 
    
    def draw_square(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.square)

    def handle_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: 
            self.square_velocity = self.jump_strength
