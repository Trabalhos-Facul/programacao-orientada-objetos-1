import pygame
import classes_jogo
import elementos_tela
import dados_cartas

LARGURA = 800
ALTURA = 500
QUADROS_POR_SEGUNDO = 60


# inicializacao da janela pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desafio Ninja")
clock = pygame.time.Clock()

# cria o juiz
juiz = classes_jogo.Juiz()

# cria as cartas todas as cartas(decks)
quantidade_cartas = dados_cartas.obter_numero_de_cartas()

deck_jogador = classes_jogo.Deck(quantidade_cartas)
deck_computador = classes_jogo.Deck(quantidade_cartas)

# por todas as sprites aqui
mao_jogador = pygame.sprite.Group()

placar_jogador = pygame.sprite.Group()
placar_computador = pygame.sprite.Group()

resultado_final = pygame.sprite.Group()

f = elementos_tela.Fogo(True)
a = elementos_tela.Agua(True)
g = elementos_tela.Gelo(True)

a_computador = elementos_tela.Agua(False)
g_computador = elementos_tela.Gelo(False)
f_computador = elementos_tela.Fogo(False)

# adiciona as 4 cartas a mao do jogador
for i in range(4):
    id_carta = deck_jogador.comprar_carta()
    c = elementos_tela.Carta(id_carta, 3, 'fogo', i)
    mao_jogador.add(c)

# adiciona os fundos dos placares
placar_jogador.add(elementos_tela.FundoPlacar(True))
placar_computador.add(elementos_tela.FundoPlacar(False))

rodando = True
esperando_carta = True

imagem_fundo = pygame.image.load(f'img/dojo.png')
imagem_fundo = pygame.transform.scale(imagem_fundo, (800, 500))

while rodando:

    clock.tick(QUADROS_POR_SEGUNDO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if event.button == 1:
                for c in mao_jogador:
                    if c.rect.collidepoint(pos) and esperando_carta:
                        c.clicked = True
                        esperando_carta = False

    for c in mao_jogador:
        if c.clicked:
            id_carta_computador = deck_computador.comprar_carta()

            carta_computador = dados_cartas.obter_valor_da_carta_e_elemento(id_carta_computador)
            carta_jogador = dados_cartas.obter_valor_da_carta_e_elemento(c.id)

            ganhador = juiz.qual_carta_ganha_a_rodada_retorna_none_caso_empate(carta_jogador, carta_computador)

            if not ganhador is None:
                if ganhador:
                    elemento_ganhador = carta_computador[1]
                    if elemento_ganhador == 'fogo':
                        placar_computador.add(f_computador)
                    elif elemento_ganhador == 'agua':
                        placar_computador.add(a_computador)
                    elif elemento_ganhador == 'gelo':
                        placar_computador.add(g_computador)
                else:
                    elemento_ganhador = carta_jogador[1]
                    if elemento_ganhador == 'fogo':
                        placar_jogador.add(f)
                    elif elemento_ganhador == 'agua':
                        placar_jogador.add(a)
                    else:
                        placar_jogador.add(g)

                juiz.contabiliza_no_placar_do_ganhador_da_rodada(ganhador, elemento_ganhador)

            print(f'Jogador: {carta_jogador}')
            print(f'Computador: {carta_computador}')
            print(f'Ganhador: {ganhador}')

            posicao_carta_jogada = c.posicao

            id_nova_carta = deck_jogador.comprar_carta()

            if id_nova_carta != -1:
                valor_nova_carta, elemento_nova_carta = dados_cartas.obter_valor_da_carta_e_elemento(id_nova_carta)
                nova_carta = elementos_tela.Carta(id_nova_carta, valor_nova_carta, elemento_nova_carta, posicao_carta_jogada)

            mao_jogador.remove(c)
            del c
            if id_nova_carta != -1:
                mao_jogador.add(nova_carta)

            if juiz.verifica_se_o_jogo_terminou():

                if juiz.quem_ganhou_a_jogo():
                    print('computador ganhou')
                    mensagem = elementos_tela.MensagemFinal(False)
                else:
                    print('jogador ganhou')
                    mensagem = elementos_tela.MensagemFinal(True)

                resultado_final.add(mensagem)
                break

            esperando_carta = True


    # atualiza o estado do jogo
    mao_jogador.update()
    placar_jogador.update()
    placar_computador.update()
    resultado_final.update()

    # desenha
    tela.blit(imagem_fundo, (0, 0))
    mao_jogador.draw(tela)
    placar_jogador.draw(tela)
    placar_computador.draw(tela)
    resultado_final.draw(tela)

    pygame.display.flip()

pygame.quit()
