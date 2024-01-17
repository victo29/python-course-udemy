from sys import path
from aula99_package.modulo import soma_do_modulo #, say_hi
from aula99_package import modulo
from aula99_package.modulo import * # Má prática de programação

### Todas as importações do programa inteiro devem ser relacionadas ao main ###

#print(*path, sep='\n')

print(soma_do_modulo(1,2))
print(modulo.soma_do_modulo(1,2))
print(variable)
#say_hi()
# print(new_variable)