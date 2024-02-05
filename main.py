import pygame
import classes_jogo
import dados_cartas
import game_sprites

# inicializacao da janela pygame
game = game_sprites.GameDrawer()

juiz = classes_jogo.Juiz()

# cria as cartas todas as cartas(decks)
quantidade_cartas = dados_cartas.obter_numero_de_cartas()

player_deck = classes_jogo.Deck(quantidade_cartas, 'player')
npc_deck = classes_jogo.Deck(quantidade_cartas, 'npc')

# adiciona as 4 cartas a mao do jogador
for i in range(4):
    card = player_deck.comprar_carta()
    game.add_to_player_hand(card)

rodando = True
clicked_card_sprite = None
click_enabled = True

while rodando:
    game.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not clicked_card_sprite and click_enabled:
            pos = pygame.mouse.get_pos()
            clicked_card_sprite = game.card_in(pos)
            
    if clicked_card_sprite:
        player_card = player_deck.get_by_id(clicked_card_sprite.id)
        npc_card = npc_deck.comprar_carta()

        winner_card = juiz.qual_carta_ganha_a_rodada_retorna_none_caso_empate(player_card, npc_card)
        juiz.record_winner_card(winner_card)

        print(f'Jogador: {player_card.element}')
        print(f'Computador: {npc_card.element}')
        print(f'Ganhador: {winner_card.owner}')
  
        game.draw_score(winner_card)
        game.draw_played_cards(player_card, npc_card)
        game.replace_player_hand(clicked_card_sprite, player_deck.comprar_carta())

        clicked_card_sprite = None

        if juiz.verifica_se_o_jogo_terminou():
            click_enabled = False
            game.draw_result_msg(juiz.quem_ganhou_a_jogo())

    game.draw()

pygame.quit()
