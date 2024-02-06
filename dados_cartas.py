import json

def obter_numero_de_cartas():
    f = open('cards.json', 'r')

    data = json.load(f)

    numero_de_cartas = len(data)

    f.close()

    return numero_de_cartas
