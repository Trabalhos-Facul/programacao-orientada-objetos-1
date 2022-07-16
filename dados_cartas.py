import json


def obter_valor_da_carta_e_elemento(id_carta):
    f = open('cards.json', 'r')

    data = json.load(f)

    valor_carta = data[id_carta - 1]['value']
    elemento_carta = data[id_carta - 1]['element']

    f.close()

    return valor_carta, elemento_carta


def obter_numero_de_cartas():
    f = open('cards.json', 'r')

    data = json.load(f)

    numero_de_cartas = len(data)

    f.close()

    return numero_de_cartas
