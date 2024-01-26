# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

# def recursiva(inicio=0, fim=10):
#     #caso_base
#     if inicio>=fim:
#         return fim

#     #caso recursivo 
#     #contar até chegar ao final
#     inicio +=1
#     return recursiva(inicio,fim)


# print(recursiva())


def fact(n):
    if n <= 1 or n <=0:
        return 1
    return n * fact(n-1)


print(fact(5))