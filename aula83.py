pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Souza',
}

chave1, chave2 = pessoa 
a,b = pessoa.values() #.items() retorna uma tupla com chave e valor
# print(a,b)

for chave, valor in pessoa.items():
    # print(chave, valor) 
    ...


pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade' : 16,
    'altura': 1.9
}

pessoas_completas = {**pessoa, **dados_pessoa}
# print(pessoas_completas)

def mostro_argumentos_nomeados(*args,**kwargs): # os dados são armazenados em dicionários
    print(f'NÃO NOMEADOS {args}')
    for chave, valor in kwargs.items():
        print(chave,valor)

mostro_argumentos_nomeados('TESTE','TESTE','TESTES',nome='Victor',idade=16,sobrenome='Tavares')

mostro_argumentos_nomeados(**pessoas_completas) #desempacotando para passar nas funçõess
