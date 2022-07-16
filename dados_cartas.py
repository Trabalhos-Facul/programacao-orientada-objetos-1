import json


def obter_valor_da_carta_e_elemento(id_carta):
    f = open('cartas.json', 'r')

    data = json.load(f)

    valor_carta = data[id_carta - 1]['valor']
    elemento_carta = data[id_carta - 1]['elemento']

    f.close()

    return valor_carta, elemento_carta


def obter_numero_de_cartas():
    f = open('cartas.json', 'r')

    data = json.load(f)

    numero_de_cartas = len(data)

    f.close()

    return numero_de_cartas