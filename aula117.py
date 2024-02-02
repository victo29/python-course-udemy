import json

# pessoa = {
#     'nome': 'Vcitor Souza',
#     'sobrenome': 'de Queiroz',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.9,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) # Manda os dados para o arquivo em formato Json
                                                               # ensure_ascii faz com que o as strings sejam em viada em um certo formato

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)



