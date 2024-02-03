nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
if idade != "" and nome != "":
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print("seu nome contem espaços " if " " in nome else "seu nome não contem espaços")
    print(f"Seu nome tem {len(nome)} quantidade de letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print("Desculpa, você deixou campos vazios")