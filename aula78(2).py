# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Victor')
s1.add(1)
s1.add(2)

#s1.update('olá mundo') # adiciona de forma iteradas
s1.update(('Olá mundo',3,4,5,6,)) # Mandando um iteravel é possível passar vários valores de uma só vez
print(s1)

#s1.clear() limpa todo o set

s1.discard('Victor') #Discarta o valor passado