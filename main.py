import pygame
import classes_jogo
import elementos_tela

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

LARGURA = 800
ALTURA = 500
QUADROS_POR_SEGUNDO = 30

# inicializacao da janela pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Legal")
clock = pygame.time.Clock()

# cria o juiz


# cria as cartas todas as cartas(decks)
deck_jogador = classes_jogo.Deck()

# por todas as sprites aqui
mao_jogador = pygame.sprite.Group()

# adiciona as 4 cartas a mao do jogador
for i in range(4):
    id_carta = deck_jogador.comprar_carta()
    c = elementos_tela.Carta(id_carta, 3, 'fogo', i)
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