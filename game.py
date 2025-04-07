import pygame
from square import Square
from pipes_entity import PipesEntity


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

        self.square = Square()
        self.pipes = PipesEntity()
        
        self.running = True
    
    def check_collision(self):
        for top_pipe, bottom_pipe in self.pipes.pipes:
            if self.square.square.colliderect(top_pipe) or self.square.square.colliderect(bottom_pipe):
                return True
        return False

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.square.handle_jump()

            # Update square position and pipes
            self.square.update_square(self.screen_height)
            self.pipes.update_pipes()

            if self.check_collision():
                self.running = False
            
            # Generate new pipes periodically
            current_time = pygame.time.get_ticks()
            if current_time - self.last_pipe_time > self.pipe_interval:
                self.pipes.generate_pipe(self.screen_height, self.screen_width)
                self.last_pipe_time = current_time
            
            self.draw()

    def draw(self):
        self.screen.fill((135, 206, 250)) 
        self.square.draw_square(self.screen)
        self.pipes.draw_pipes(self.screen)
        pygame.display.update()

    def quit(self):
        pygame.quit()
    




