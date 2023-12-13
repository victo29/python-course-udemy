nome = input("Digite o seu primeiro nome: ")

nome_curto = len(nome) <= 4
nome_normal = len(nome) > 4 and len(nome) < 7
nome_grande = len(nome) > 6

if nome_curto:
    print("Seu nome é curto")
elif nome_normal:
    print("Seu nome é normal")
elif nome_grande:
    print("Seu nome é grande")