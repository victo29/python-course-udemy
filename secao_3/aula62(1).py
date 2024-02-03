CPF = '746.824.890-70'.replace('.','')\
    .replace('-','')

cpf_formatado = []
for i in range(11):
        cpf_formatado.append(CPF[i])
cpf_formatado_copia = cpf_formatado.copy()

contador = 0
soma_dos_digitos = 0
for j in range(10,1, -1):
    cpf_formatado[contador] = int(cpf_formatado[contador]) * j
    soma_dos_digitos+= cpf_formatado[contador]
    contador+=1

soma_dos_digitos = (soma_dos_digitos * 10) % 11
resultado_primeiro_digito = soma_dos_digitos if soma_dos_digitos <= 9 else 0


contador = 0
soma_dos_digitos = 0
for j in range(11,1, -1):
    cpf_formatado_copia[contador] = int(cpf_formatado_copia[contador]) * j
    soma_dos_digitos+= cpf_formatado_copia[contador]
    contador+=1

soma_dos_digitos = (soma_dos_digitos * 10) % 11
resultado_segundo_digito = soma_dos_digitos if soma_dos_digitos <= 9 else 0


cpf_gerado = f'{CPF[:9]}{resultado_primeiro_digito}{resultado_segundo_digito}'
if cpf_gerado == CPF:
    print('O cpf é valido')
else:
    print('O cpf é invalido')


"""
.replace('.','') substitui o caractere passado por um outro que foi passado
"""