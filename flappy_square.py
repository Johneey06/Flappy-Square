import pygame
import random

'''
TODO

Add point scoring
death screen and title screen
lose if touch top or bottom
spawn pipe immediately when game start
'''
class Game: 
    def __init__(self):
        pygame.init()

        # Iniatialize screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Flappy square")
        self.clock = pygame.time.Clock()

        # Time of the last pipe generation (in milliseconds)
        self.last_pipe_time = 0
        self.pipe_interval = 2000

        # Initialize square attributes
        self.square_width = 30
        self.square_height = 30
        self.square_x = 50
        self.square_y = 300
        self.square_velocity = 0

        self.gravity = 0.5
        self.jump_strength = -5

        self.square = pygame.Rect(self.square_x, self.square_y, self.square_width, self.square_height)

        # Initialize pipe attributes
        self.pipe_width = 60
        self.pipe_gap = 150
        self.pipe_velocity = 3
        self.pipes = []
    
    def update_square(self):
        self.square_velocity += self.gravity
        self.square.y += self.square_velocity

        # Ground collision
        if self.square.y > self.screen_height - self.square_height:
            self.square.y = self.screen_height - self.square_height
        # Ceiling collision
        elif self.square.y < 0:
            self.square.y = 0 

    def handle_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: 
            self.square_velocity = self.jump_strength

    def generate_pipe(self):
        # y position of where gap starts

        gap_y = random.randint(0, self.screen_height - self.pipe_gap)

        top_pipe = pygame.Rect(self.screen_width, gap_y - self.screen_height, self.pipe_width, self.screen_height)
        bottom_pipe = pygame.Rect(self.screen_width, gap_y + self.pipe_gap, self.pipe_width, self.screen_height)

        self.pipes.append((top_pipe, bottom_pipe))

    def draw_pipes(self):
        for top_pipe, bottom_pipe in self.pipes:
            pygame.draw.rect(self.screen, (0, 255, 0), top_pipe)
            pygame.draw.rect(self.screen, (0, 255, 0), bottom_pipe)

    def update_pipes(self):
        for top_pipe, bottom_pipe in self.pipes:
            top_pipe.x -= self.pipe_velocity
            bottom_pipe.x -= self.pipe_velocity

        # Remove off-screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe[0].x > -self.pipe_width]

    def check_collision(self):
        for top_pipe, bottom_pipe in self.pipes:
            if self.square.colliderect(top_pipe) or self.square.colliderect(bottom_pipe):
                return True
        return False

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_jump()
            
            # Update square position and pipes
            self.update_square()
            self.update_pipes()
            
            if self.check_collision():
                running = False
            
            # Generate new pipes periodically
            current_time = pygame.time.get_ticks()
            if current_time - self.last_pipe_time > self.pipe_interval:
                self.generate_pipe()
                self.last_pipe_time = current_time
 
            self.screen.fill((135, 206, 250)) 
            
            pygame.draw.rect(self.screen, (255, 255, 0), self.square)
            self.draw_pipes()
            
            pygame.display.update()

        pygame.quit()

Game().run()

