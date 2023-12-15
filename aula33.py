"""
Imutaveis: str, int, float, bool
"""

string = 'Victor'
# string[3] = '*' Nãa é possível
outra_variavel = f'{string[:3]}*{string[4:]}'
print(outra_variavel)
