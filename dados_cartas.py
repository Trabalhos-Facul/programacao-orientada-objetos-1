import json


def obter_valor_da_carta_e_elemento(id_carta):
    f = open('cartas.json', 'r')

    data = json.load(f)

    valor_carta = print(data[id_carta-1]['valor'])
    elemento_carta = print(data[id_carta-1]['elemento'])

    f.close()

    return valor_carta, elemento_carta


