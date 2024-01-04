# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"

# pessoa = dict(nome='Victor',sobrenome='Souza')
pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Souza',
    'idade': 16,
    'enderecos':[
        {'rua':'girimun','numero':123},
        {'rua':'gaiamun','numero':456}  
                 ],
}

print(pessoa['nome'])
print(10*'-')
for chave in pessoa:
    print(chave, pessoa[chave])