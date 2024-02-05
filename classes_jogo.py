import random
from typing import Any
import json

class Juiz:
    def __init__(self):
        self.placar_jogador = [False, False, False]
        self.placar_bot = [False, False, False]
        self.elementos_cartas = ['agua', 'fogo', 'gelo']

    def qual_carta_ganha_a_rodada_retorna_none_caso_empate(self, carta_jogador, carta_bot):
        jogador_ganhou = 0
        bot_ganhou = 1

        resultado = self.qual_elemento_ganha_retorna_none_caso_empate(carta_jogador.element, carta_bot.element)

        mesmo_elemento = resultado is None
        elemento_do_jogador_ganha = resultado == 0

        if mesmo_elemento:
            if carta_jogador.element == carta_bot.value:
                return None

            if carta_jogador.element > carta_bot.value:
                return jogador_ganhou

        if elemento_do_jogador_ganha:
            return jogador_ganhou
        else:
            return bot_ganhou

    def stroger_card(self, card_0, card_1):
        result = self.stronger_element(card_0, card_1)

        if result is None:
            return self.stroger_value(card_0, card_1)
        else:
            return result

    def stronger_element(self, card_0, card_1):
        if card_0.element == card_1.element: 
            return None

    def stronger_value(self, card_0, card_1):
        if card_0.value == card_1.value:
            return None
        
        if card_0.value > card_1.value:
            return card_0
        else:
            return card_1

    def qual_elemento_ganha_retorna_none_caso_empate(self, elemento_0, elemento_1):
        index_elemento_0 = self.elementos_cartas.index(elemento_0)
        index_elemento_1 = self.elementos_cartas.index(elemento_1)

        if index_elemento_0 == index_elemento_1:
            return None

        if index_elemento_1 == (index_elemento_0+1)//3 or index_elemento_0+1 == index_elemento_1-1:
            return 1
        else:
            return 0

    def contabiliza_no_placar_do_ganhador_da_rodada(self, ganhador, elemento):
        index_para_ser_contabilizado = self.elementos_cartas.index(elemento)
        jogador_ganhou = ganhador == 0
        bot_ganhou = ganhador == 1

        if jogador_ganhou:
            self.placar_jogador[index_para_ser_contabilizado] = True

        elif bot_ganhou:
            self.placar_bot[index_para_ser_contabilizado] = True

    def verifica_se_o_jogo_terminou(self):
        if all(self.placar_jogador) or all(self.placar_bot):
            return True
        else:
            return False

    def quem_ganhou_a_jogo(self):
        if all(self.placar_jogador):
            return "player"
        elif all(self.placar_bot):
            return "npc"
        else:
            return None

class Deck:
    def __init__(self, tamnho_deck, owner):
        self.owner = owner
        self.cartas = []
        self.cards_attrs = self.load_cards_attrs()
        
        for i in range(1, tamnho_deck+1):
            self.cartas.append(i)

    def load_cards_attrs(self):
        f = open('cards.json', 'r')
        cards_attrs = json.load(f)
        f.close()
        return cards_attrs

    def comprar_carta(self):
        if self.cartas:
            card_id = random.randint(0,len(self.cartas)-1)
            return Card(card_id, self.owner, self.cards_attrs[card_id - 1])
        else:
            return -1
        
    def get_by_id(self, card_id):
        return  Card(card_id, self.owner, self.cards_attrs[card_id - 1])

class Card:
    def __init__(self, id, owner, card_attr) -> None:
        self.id = id
        self.owner = owner
        self.value = card_attr['value']
        self.element = card_attr['element']
