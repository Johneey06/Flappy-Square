import pygame
from square import Square
from pipes_entity import PipesEntity


class Game:
    def __init__(self):
        pygame.init()

        # Iniatialize screen settings
        self.screen_width = 800
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

        self.score = 0

        # Text
        self.font = pygame.font.Font(None, 74)
        self.color = (0, 0, 0)
        self.text_surface = self.font.render(str(self.score), True, self.color)

        self.passed_pipe = False

    
    def check_death_collision(self):
        isDead = False
        # Ground collision and Ceiling collision
        if self.square.square.y >= self.screen_height - self.square.square_height or self.square.square.y <= 0:
            isDead = True

        # Pipe collision
        for top_pipe, bottom_pipe in self.pipes.pipes:
            if self.square.square.colliderect(top_pipe) or self.square.square.colliderect(bottom_pipe):
                isDead = True

        return isDead
    
    def score_collision(self):
        # Pass front pipe 
        if self.square.square.x > self.pipes.pipes[0][0].x and not self.passed_pipe:
            self.score += 1
            self.passed_pipe = True
        
        if self.square.square.x <= self.pipes.pipes[0][0].x:
            self.passed_pipe = False


    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.square.handle_jump()

            # Update square position and pipes
            self.square.update_square()
            self.pipes.update_pipes()

            if self.check_death_collision():
                self.running = False
            
            
            if len(self.pipes.pipes) == 0:
                self.pipes.generate_pipe(self.screen_height, self.screen_width)

            # Generate new pipes periodically
            current_time = pygame.time.get_ticks()
            if current_time - self.last_pipe_time > self.pipe_interval:
                self.pipes.generate_pipe(self.screen_height, self.screen_width)
                self.last_pipe_time = current_time

            self.score_collision()
            self.draw()

    def draw(self):
        self.screen.fill((135, 206, 250)) 
        self.square.draw_square(self.screen)
        self.pipes.draw_pipes(self.screen)

        self.text_surface = self.font.render(str(self.score), True, self.color)
        self.screen.blit(self.text_surface, (10, 0))
        pygame.display.update()

    def quit(self):
        pygame.quit()
    




