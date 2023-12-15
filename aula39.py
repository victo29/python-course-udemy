string = input("Digite um nome qualquer: ")
quantidade_de_letras = len(string)

nova_string = ''
contador = 0

while contador < quantidade_de_letras:
    nova_string += f'*{string[contador]}'
    contador+=1

print(nova_string)