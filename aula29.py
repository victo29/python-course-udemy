"""Introdução ao try/except"""

numero = input('Dobrarei o número que vc digitar: ')

try:
    numero_float = float(numero)
    print(f"O dobro do número é {numero_float * 2}")
except:
    print("Isso não é um número")