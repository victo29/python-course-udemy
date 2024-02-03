# Generator expression, Iterables e Iterators em Python

import sys
iterable = ['Olá','Mundo','Legal']
iterator = iter(iterable) #Nâo sabe nada sobre o iteravel, somente consegue entregar o próximo valor

lista = [n for n in range(100)] #Ao criar uma lista ela já fica salva na memória
generator = (n for n in range(100)) #só te entraga um valor por vez


print(sys.getsizeof(lista)) # Retorna o tamanho do elemento em espaço de armazenamento
print(sys.getsizeof(generator))


print(next(generator))
print(next(generator))
print(next(generator))
