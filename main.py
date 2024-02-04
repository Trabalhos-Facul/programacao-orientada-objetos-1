import pygame
import classes_jogo
import elementos_tela
import dados_cartas
import game

# inicializacao da janela pygame
game = game.GameDrawer()

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
cartas_rodada = pygame.sprite.Group()

f = elementos_tela.Fogo(True)
a = elementos_tela.Agua(True)
g = elementos_tela.Gelo(True)

a_computador = elementos_tela.Agua(False)
g_computador = elementos_tela.Gelo(False)
f_computador = elementos_tela.Fogo(False)

# adiciona as 4 cartas a mao do jogador
for i in range(4):
    id_carta = deck_jogador.comprar_carta()
    c = elementos_tela.Carta(id_carta, 3, i)
    mao_jogador.add(c)

# adiciona os fundos dos placares
placar_jogador.add(elementos_tela.FundoPlacar(True))
placar_computador.add(elementos_tela.FundoPlacar(False))

rodando = True
clicked_card = None
click_enabled = True

while rodando:
    game.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not clicked_card and click_enabled:
            pos = pygame.mouse.get_pos()
            # retornar a carta clicada
            # clicked_card = game.card_in(pos)
            for c in mao_jogador:
                if c.rect.collidepoint(pos):
                    clicked_card = c
                    break

    if clicked_card:
        id_carta_computador = deck_computador.comprar_carta()

        carta_computador = dados_cartas.obter_valor_da_carta_e_elemento(id_carta_computador)
        carta_jogador = dados_cartas.obter_valor_da_carta_e_elemento(clicked_card.id)

        ganhador = juiz.qual_carta_ganha_a_rodada_retorna_none_caso_empate(carta_jogador, carta_computador)

        carta_jogador_mostrar = elementos_tela.CartaJogada(True, clicked_card.image)
        carta_computador_mostrar = elementos_tela.CartaJogada(False, dados_cartas.imagem_carta(id_carta_computador))

        cartas_rodada.add(carta_jogador_mostrar)
        cartas_rodada.add(carta_computador_mostrar)

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

        posicao_carta_jogada = clicked_card.posicao

        id_nova_carta = deck_jogador.comprar_carta()

        if id_nova_carta != -1:
            valor_nova_carta, _ = dados_cartas.obter_valor_da_carta_e_elemento(id_nova_carta)
            nova_carta = elementos_tela.Carta(id_nova_carta, valor_nova_carta, posicao_carta_jogada)

        mao_jogador.remove(clicked_card)
        clicked_card = None

        if id_nova_carta != -1:
            mao_jogador.add(nova_carta)

        if juiz.verifica_se_o_jogo_terminou():
            click_enabled = False

            if juiz.quem_ganhou_a_jogo():
                print('computador ganhou')
                mensagem = elementos_tela.MensagemFinal(False)
            else:
                print('jogador ganhou')
                mensagem = elementos_tela.MensagemFinal(True)

            resultado_final.add(mensagem)

    # atualiza o estado do jogo
    mao_jogador.update()
    placar_jogador.update()
    placar_computador.update()
    cartas_rodada.update()
    resultado_final.update()

    # desenha
    placar_jogador.draw(game.display)
    placar_computador.draw(game.display)
    mao_jogador.draw(game.display)
    cartas_rodada.draw(game.display)
    resultado_final.draw(game.display)

    game.draw()

pygame.quit()
