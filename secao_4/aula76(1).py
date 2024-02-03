# Manipulando chaves e valores em dicionários

# pessoa = {
#     'nome': 'Victor',
#     'sobrenome': 'Souza',
#     'idade': 16,
#     'enderecos':[
#         {'rua':'girimun','numero':123},
#         {'rua':'gaiamun','numero':456}  
#                  ],
# }

pessoa = {}

chave = 'nome'
pessoa[chave] = 'Victor Souza'
print(pessoa[chave])

# pessoa[chave] = 'Victor Tavares'
# print(pessoa[chave])

pessoa['sobrenome'] = 'Tavares'
#del pessoa['sobrenome']

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print('Existe')