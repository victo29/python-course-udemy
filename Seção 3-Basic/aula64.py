#Gerador de CPF

import random

cpf_gerado = ''
for i in range(9):
    cpf_gerado += str(random.randint(0,10))


cpf_formatado = []
for i in range(9):
        cpf_formatado.append(cpf_gerado[i])

contador = 0
soma_dos_digitos = 0
for j in range(10,1, -1):
    soma_dos_digitos += int(cpf_formatado[contador]) * j
    contador+=1

soma_dos_digitos = (soma_dos_digitos * 10) % 11
resultado_primeiro_digito = soma_dos_digitos if soma_dos_digitos <= 9 else 0
cpf_formatado.append(str(resultado_primeiro_digito))


contador = 0
soma_dos_digitos = 0
for j in range(11,1, -1):
    soma_dos_digitos += int(cpf_formatado[contador]) * j
    contador+=1

soma_dos_digitos = (soma_dos_digitos * 10) % 11
resultado_segundo_digito = soma_dos_digitos if soma_dos_digitos <= 9 else 0
cpf_formatado.append(str(resultado_segundo_digito))
cpf_formatado = "".join(cpf_formatado) 
print(f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:11]}")
