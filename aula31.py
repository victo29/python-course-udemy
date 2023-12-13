"""
Flag(Bandeira) - Marcar um local
None = não valor
is e is nor = é ou não é
id = identidade
"""

# v1 = 'a'
# v2 = 'a'

# print(id(v1))
# print(id(v2))

################################

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)