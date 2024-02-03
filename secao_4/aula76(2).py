# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Souza',
    'enderecos':[
        {'rua':'girimun','numero':123},
        {'rua':'gaiamun','numero':456}  
                 ],
}

# print(len(pessoa))  #Retorna a quantidade de chaves
# chaves = list(pessoa.keys()) #retorna as chaves
# print(chaves[0])



# print(pessoa.values()) #retorna os valores 



# print(pessoa.items())#retorna as chaves junto aos valoress

# for chave, valor in pessoa.items():
#     print(chave,valor)


# pessoa.setdefault('idade', 16)
# print(pessoa['idade'])



# print(pessoa.get('nome','não existe')) #Evita erros caso a chave não exista


# endereco = pessoa.pop('enderecos') #Exclui e retorna a chave excluida 
# print(endereco)


# ultima_chave = pessoa.popitem() #Exclui e retorna a ultima chave 
# print(ultima_chave)


pessoa.update({  #Altera e adiciona chaves a um dicionário
    'nome':'Kloviz',
    'idade':'16',
})

# pessoa.update(sexo='Masculino')
tupla = ('sexo','Masculino'),

pessoa.update(tupla)
print(pessoa)