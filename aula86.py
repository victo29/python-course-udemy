# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}




dc = {
    chave:valor.upper()
    if isinstance(valor,str) else valor #isinstance(valor,classe ) verifica se o elemento corresponde a classe passada
    for chave,valor in produto.items()

}
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b')

]

dc2 = {
    chave:valor
    for chave,valor in lista
}

print(dict(lista))
print(dc2)


s1 = {
    i for i in range(10)
}
print(s1)
