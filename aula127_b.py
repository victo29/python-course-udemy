import json
from aula127_a import Pessoa, CAMINHO_ARQUIVO, fazer_dump


# CAMINHO_DO_ARQUIVO = 'aula127.json'

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])

print(p1.nome)
print(p2.nome)