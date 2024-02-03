#Calculando o primeiro digito de um CPF
#CPF = 746.824.890-70

CPF = '746.824.890-70'
cpf_formatado = []
for i in range(11):
    if CPF[i] == '.':
        continue
    else:
        cpf_formatado.append(CPF[i])


contador = 0
soma_dos_digitos = 0
for j in range(10,1, -1):
    cpf_formatado[contador] = int(cpf_formatado[contador]) * j
    soma_dos_digitos+= cpf_formatado[contador]
    contador+=1

soma_dos_digitos *= 10
operacao = soma_dos_digitos % 11
resultado_primeiro_digito = operacao if operacao <= 9 else 0
print(resultado_primeiro_digito)

