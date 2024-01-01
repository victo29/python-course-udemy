while True:
    numero = input("Digite um número inteiro: ")
    try:
        numero = int(numero)
        texto = "É um número "
        print(texto + 'par' if numero % 2 == 0 else texto + 'impar')
        break
    except:
        print("O número digitado não é inteiro")