import pygame
import random

class PipesEntity:
    def __init__(self):
    # Initialize pipe attributes
        self.pipe_width = 60
        self.pipe_gap = 150
        self.pipe_velocity = 3
        self.pipes = []

        

    def generate_pipe(self, screen_height, screen_width):
        # y position of where gap starts
        gap_y = random.randint(0, screen_height - self.pipe_gap)

        top_pipe = pygame.Rect(screen_width, gap_y - screen_height, self.pipe_width, screen_height)
        bottom_pipe = pygame.Rect(screen_width, gap_y + self.pipe_gap, self.pipe_width, screen_height)
        
        self.pipes.append((top_pipe, bottom_pipe))

    def draw_pipes(self, screen):
        for top_pipe, bottom_pipe in self.pipes:
            pygame.draw.rect(screen, (0, 255, 0), top_pipe)
            pygame.draw.rect(screen, (0, 255, 0), bottom_pipe)

    def update_pipes(self):
        for top_pipe, bottom_pipe in self.pipes:
            top_pipe.x -= self.pipe_velocity
            bottom_pipe.x -= self.pipe_velocity

        # Remove off-screen pipes
        self.pipes = [pipe for pipe in self.pipes if pipe[0].x > -self.pipe_width]
    


