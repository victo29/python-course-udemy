import pprint
def p(valor):
    pprint.pprint(valor,sort_dicts=False,width=40)




# Mapeamento de dados em list comprehension
# O que vem na esquerda do for é mapeamento o que vem na esquerda é filtro
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, }
]

# novos_produtos = [
#     {'nome':produto['nome'], 'preco':produto['preco']*2}
#     for produto in produtos]


novos_produtos = [
    {**produto, 'preco':produto['preco']*1.15}
    if produto['preco'] < 20 else {**produto} 
    for produto in produtos]

p(novos_produtos)
print()

novos_produtos_1 = [
    {**produto, 'preco':produto['preco']*1.15}
    if produto['preco'] < 20 else {**produto} 
    for produto in produtos
    if produto['preco'] >15]

p(novos_produtos_1)