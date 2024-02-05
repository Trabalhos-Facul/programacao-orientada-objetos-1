import pygame

class Fogo(pygame.sprite.Sprite):
    def __init__(self, jogador):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'img/fogo.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        if jogador:
            self.rect.center = 200, 100
        else:
            self.rect.center = 600, 100


class Agua(pygame.sprite.Sprite):
    def __init__(self, jogador):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'img/agua.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        if jogador:
            self.rect.center = 100,100
        else:
            self.rect.center = 700,100


class Gelo(pygame.sprite.Sprite):
    def __init__(self, jogador):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f'img/gelo.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        if jogador:
            self.rect.center = 300,100
        else:
            self.rect.center = 500,100


class MensagemFinal(pygame.sprite.Sprite):
    def __init__(self, jogador: object) -> object:

        pygame.sprite.Sprite.__init__(self)

        if jogador:
            self.image = pygame.image.load(f'img/voce_ganhou.png').convert()
        else:
            self.image = pygame.image.load(f'img/voce_perdeu.png').convert()

        self.rect = self.image.get_rect()

        self.rect.center = 400, 250


class FundoPlacar(pygame.sprite.Sprite):
    def __init__(self, jogador):

        pygame.sprite.Sprite.__init__(self)

        if jogador:
            self.image = pygame.image.load(f'img/placar_jogador.png').convert()
            self.rect = self.image.get_rect()
            self.rect.center = 200, 100
        else:
            self.image = pygame.image.load(f'img/placar_computador.png').convert()
            self.rect = self.image.get_rect()
            self.rect.center = 600, 100
