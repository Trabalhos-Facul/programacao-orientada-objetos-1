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


class Carta:
    def __init__(self, id_carta, valor, elemento):
        self.id = id_carta
        self.valor = valor
        self.elemento = elemento
