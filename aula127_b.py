import json
from aula127_a import Pessoa

# class Pessoa:
#     ano_atual = 2024

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# def recupera_atributos(caminho_do_arquivo):
#     with open(caminho_do_arquivo,'r', encoding='utf8') as arquivo:
#         pessoa = json.load(arquivo)
#     return pessoa

CAMINHO_DO_ARQUIVO = 'aula127.json'
atributos = Pessoa.recupera_atributos(CAMINHO_DO_ARQUIVO)
pessoa1 = Pessoa(**atributos)

print(pessoa1.nome)
print(pessoa1.idade)
