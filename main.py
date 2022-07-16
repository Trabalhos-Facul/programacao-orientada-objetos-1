import pygame
import classes_jogo
import elementos_tela
import dados_cartas

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

LARGURA = 800
ALTURA = 500
QUADROS_POR_SEGUNDO = 60

# inicializacao da janela pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Legal")
clock = pygame.time.Clock()

# cria o juiz
juiz = classes_jogo.Juiz()

# cria as cartas todas as cartas(decks)
quantidade_cartas = dados_cartas.obter_numero_de_cartas()

deck_jogador = classes_jogo.Deck(quantidade_cartas)
deck_computador = classes_jogo.Deck(quantidade_cartas)

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

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        if event.button == 1:
            for c in mao_jogador:
                if c.rect.collidepoint(pos):
                    c.clicked = True

    for c in mao_jogador:
        if c.clicked:
            print(f'carta {c.id}, valor {c.valor} elemento {c.elemento} foi clicada')
            mao_jogador.remove(c)

    # atualiza o estado do jogo
    mao_jogador.update()

    # desenha
    tela.fill(PRETO)
    mao_jogador.draw(tela)

    pygame.display.flip()

pygame.quit()