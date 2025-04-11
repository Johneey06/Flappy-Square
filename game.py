import pygame
from square import Square
from pipes_entity import PipesEntity
from projectile import Projectile


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

        # Time of the last projectile generation (in milliseconds)
        self.last_projectile_time = 0 
        self.projectile_interval = 2500

        self.square = Square()
        self.pipes = PipesEntity()
        self.projectiles = Projectile()
        
        self.running = True
        self.death_screen = False

        self.score = 0

        # Score Text
        self.font = pygame.font.Font(None, 74)
        self.color = (0, 0, 0)
        self.score_text = self.font.render(str(self.score), True, self.color)

        # Death Screen Text
        self.death_text = self.font.render("You died", True, self.color)
        self.death_rect = self.death_text.get_rect()
        self.death_rect.center = (self.screen_width / 2, self.screen_height / 2 - 200)

        # Press R to restart
        self.restart_text = self.font.render('Press "R" to restart game', True, self.color)
        self.restart_rect = self.restart_text.get_rect()
        self.restart_rect.center = (self.screen_width / 2, self.screen_height / 2)

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

        # Projectile Collision
        for projectile in self.projectiles.projectiles:
            if self.square.square.colliderect(projectile):
                isDead = True

        return isDead
    
    def score_collision(self):
        # Pass front pipe 
        if self.square.square.x > self.pipes.pipes[0][0].x and not self.passed_pipe:
                self.score += 1
                self.passed_pipe = True
        
        if self.square.square.x <= self.pipes.pipes[0][0].x:
            self.passed_pipe = False

    def draw(self):
        self.screen.fill((135, 206, 250)) 
        self.square.draw_square(self.screen)
        self.pipes.draw_pipes(self.screen)
        self.projectiles.draw_projectiles(self.screen)

        self.score_text = self.font.render(str(self.score), True, self.color)
        self.screen.blit(self.score_text, (10, 0))
        pygame.display.update()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.square.handle_jump()
            
            if self.death_screen:
                self.death_menu()
            else:
                self.game_loop()
        
    def death_menu(self):
        self.score = 0
        self.square = Square()
        self.pipes = PipesEntity()
        self.projectiles = Projectile()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]: 
            self.death_screen = False
        self.screen.fill((255, 0, 0))

        self.screen.blit(self.death_text, self.death_rect)
        self.screen.blit(self.restart_text, self.restart_rect)

        pygame.display.update()
        self.last_pipe_time = pygame.time.get_ticks() 
        self.last_projectile_time = pygame.time.get_ticks() 

    def game_loop(self):
        # Update square position and pipes
        dt = self.clock.tick(60) / 1000
        self.square.update_square(dt)
        self.projectiles.update_projectiles(dt)
        self.pipes.update_pipes(dt)

        if self.check_death_collision():
            self.death_screen = True

                
        if len(self.pipes.pipes) == 0:
            self.pipes.generate_pipe(self.screen_height, self.screen_width)

        # Generate new pipes periodically
        current_time = pygame.time.get_ticks()
        if current_time - self.last_pipe_time > self.pipe_interval:
            self.pipes.generate_pipe(self.screen_height, self.screen_width)
            self.last_pipe_time = current_time

        #  Generate new projectiles periodically
        if current_time - self.last_projectile_time > self.projectile_interval:
            self.projectiles.generate_projectiles(self.screen_height, self.screen_width)
            self.last_projectile_time = current_time

        self.score_collision()
        self.draw()

    def quit(self):
        pygame.quit()
    




