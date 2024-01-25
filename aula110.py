from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# teste = ['a','a','a','a','b','c','c','a']
# grupos = groupby(sorted(teste)) # tem que estar de maneira ordenada

# for chave, grupo in grupos: # vem em formato de tupla
#     print(chave)
#     print(list(grupo))

alunos_agrupados = sorted(alunos, key=lambda a:a['nota'])
grupos = groupby(alunos_agrupados, key= lambda a:a['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)