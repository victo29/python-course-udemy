# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
def executa(function,num):
    return function(num)


lista = [numero if executa(lambda x : x%2==0,numero) else 'Impar'
         for numero in range(10)]

print(lista)
