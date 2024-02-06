import classes_jogo
import dados_cartas

class Game:
    def __init__(self, drawer) -> None:
        self.rules = classes_jogo.Juiz()
        self.drawer = drawer
        self.config_deck()
        self.fill_player_hand()

    def config_deck(self):
        quantidade_cartas = dados_cartas.obter_numero_de_cartas()

        self.player_deck = classes_jogo.Deck(quantidade_cartas, 'player')
        self.npc_deck = classes_jogo.Deck(quantidade_cartas, 'npc')

    def fill_player_hand(self):
        for _ in range(4):
            card = self.player_deck.comprar_carta()
            self.drawer.add_to_player_hand(card)

    def run_round(self, clicked_card_sprite):
        player_card = self.player_deck.get_by_id(clicked_card_sprite.id)
        npc_card = self.npc_deck.comprar_carta()

        winner_card = self.rules.qual_carta_ganha_a_rodada_retorna_none_caso_empate(player_card, npc_card)
        self.rules.record_winner_card(winner_card)

        print("------------------------------")
        print(f'Jogador: {player_card.element}')
        print(f'Computador: {npc_card.element}')
        print(f'Ganhador: {winner_card.owner}')

        self.drawer.draw_score(winner_card)
        self.drawer.draw_played_cards(player_card, npc_card)
        self.drawer.replace_player_hand(clicked_card_sprite, self.player_deck.comprar_carta())

        if self.is_game_finished():
            self.drawer.draw_result_msg(self.rules.quem_ganhou_a_jogo())

    def is_game_finished(self):
        return self.rules.verifica_se_o_jogo_terminou()