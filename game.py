import pygame

class Game:
    FPS = 60
    WIDTH = 800
    HEIGHT = 500

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.load_background_img()
        pygame.display.set_caption("Desafio Ninja")
        pygame.init()
        
    def config_display(self):
        pass

    def load_background_img(self):
        dojo = pygame.image.load(f'img/dojo.png')
        bg_img = pygame.transform.scale(dojo, (self.WIDTH, self.HEIGHT))
        self.display.blit(bg_img, (0, 0))

    def tick(self):
        self.clock.tick(self.FPS)
    
    def draw(self):
        pygame.display.flip()