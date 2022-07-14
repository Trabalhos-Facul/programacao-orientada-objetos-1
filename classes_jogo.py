import pygame
import random


class Juiz:
    def __init__(self):
        self.placar_jogador = [False, False, False]
        self.placar_bot = [False, False, False]
        self.elementos_cartas = ['agua', 'fogo', 'gelo']

    def qual_carta_ganha_a_rodada_retorna_none_caso_empate(self, carta_jogador, carta_bot):
        jogador_ganhou = 0
        bot_ganhou = 1

        resultado = self.qual_elemento_ganha_retorna_none_caso_empate(carta_jogador.elemento, carta_bot.elemento)

        mesmo_elemento = resultado is None
        elemento_do_jogador_ganha = resultado == 0

        if mesmo_elemento:
            if carta_jogador.valor == carta_bot:
                return None

            if carta_jogador.valor > carta_bot.valor:
                return jogador_ganhou

        if elemento_do_jogador_ganha:
            return jogador_ganhou
        else:
            return bot_ganhou

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
        self.image = pygame.image.load(f'img/Card-Jitsu_Cards_full_{id_carta}.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (largura_offset_inicial + (posicao_carta * 125), (altura_tela * 3) // 4)


class Deck:
    def __init__(self):
        self.cartas = []
        for i in range(1,5):
            self.cartas.append(i)

    def comprar_carta(self):
        if self.cartas:
            x = random.randint(0,len(self.cartas)-1)
            return self.cartas.pop(x)
        else:
            return -1

