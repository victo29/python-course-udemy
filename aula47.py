#Adivinhe a palavra secreta
import os

palavra_secreta = 'Kloviz'.upper()
letras_acertadas = ''
contador = 0
while True:

    letra_digitada = input("Digite uma letra: ").upper()
    if  len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    contador+= 1
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada +='*'
    print(palavra_formatada)
    
    if palavra_formatada == palavra_secreta:
        os.system('cls')
        break
print(f'A palavra era {palavra_secreta} \nVocê acertou em {contador} tentativas')
