import pygame
import classes_jogo

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

LARGURA = 500
ALTURA = 480
QUADROS_POR_SEGUNDO = 30

POSICAO = (LARGURA//2, ALTURA//2)

# inicializacao da janela pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Legal")
clock = pygame.time.Clock()

# por todas as sptrites aqui
mao_jogador = pygame.sprite.Group()

# cria as cartas
c = classes_jogo.Carta(1, 3, 'fogo', POSICAO)

# adiciona cartas a mao
mao_jogador.add(c)

rodando = True
while rodando:

    clock.tick(QUADROS_POR_SEGUNDO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # atualiza o estado do jogo
    mao_jogador.update()

    # desenha
    tela.fill(PRETO)
    mao_jogador.draw(tela)

    pygame.display.flip()

pygame.quit()