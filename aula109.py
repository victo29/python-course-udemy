# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['P','M','G'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão','poliéster']
]

# print_iter(combinations(pessoas, 3)) #não pode ter repetições
# print()
# print_iter(permutations(pessoas, 2)) #pode ter repetições
# print()
print_iter(product(*camisetas))