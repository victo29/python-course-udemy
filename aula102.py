# Variáveis livres + nonlocal

# def fora(x):
#     a = x
#     # A is a free vars
#     def dentro():
#         print(locals())
#         return a    
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())

def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar # A variavel valor final não pode ser alterada 
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('d'))
print(c('c'))