""" Calculadora com While """

while True: 
    primeiro_numero = input("Digite o primeiro número: ")
    segundo_numero = input("Digite o segundo número: ")
    operador = input("Qual operador você deseja utilizar [*] [/] [+] [-]: ")

    try:
        primeiro_numero = float(primeiro_numero)
        segundo_numero = float(segundo_numero)
        
        if operador == '*':
            print(primeiro_numero*segundo_numero)
        elif operador == '/':
            print(primeiro_numero/segundo_numero)
        elif operador == '+':
            print(primeiro_numero+segundo_numero)
        elif operador == '-':
            print(primeiro_numero-segundo_numero) 
        else:
            print("O operador digitado é invalido!")
            continue

        sair = input("Deseja sair: [s]").lower().startswith('s')
        if sair:
            break
    except :
        print("um ou ambos dos números que você digitou não são validos, tente novamente!")
    