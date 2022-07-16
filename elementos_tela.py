import pygame
# heranca sendo utilizada
class Carta(pygame.sprite.Sprite):
    def __init__(self, id_carta, valor, elemento, posicao_carta):
        altura_tela = 500
        largura_offset_inicial = 225

        pygame.sprite.Sprite.__init__(self)
        self.clicked = False
        self.id = id_carta
        self.valor = valor
        self.elemento = elemento
        self.posicao = posicao_carta
        self.image = pygame.image.load(f'img/Card-Jitsu_Cards_full_{id_carta}.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (largura_offset_inicial + (posicao_carta * 125), (altura_tela * 3) // 4)