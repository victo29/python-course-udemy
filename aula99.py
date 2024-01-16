from sys import path
from aula99_package.modulo import soma_do_modulo 
from aula99_package import modulo
from aula99_package.modulo import * # Má prática de programação


#print(*path, sep='\n')

print(soma_do_modulo(1,2))
print(modulo.soma_do_modulo(1,2))
print(variable)
# print(new_variable)