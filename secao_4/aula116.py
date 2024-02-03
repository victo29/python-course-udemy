import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho = "D:\\Victor\\Documents\\VSAprendizado\\Estudos\\Python_Udemy\\"
caminho += 'aula116.txt'

# arquivo = open(caminho, 'w')

# arquivo.close()

# with  open(caminho, 'w+') as arquivo:
#     arquivo.write('linha 1\n')
#     arquivo.write('linha 2\n')
#     arquivo.writelines(
#         ('linha 3\n', 'linha 4')
#     )

#     arquivo.seek(0,0) # Retorna o cursor para o topo do Arquivo
#     print(arquivo.read())

#     print('Lendo(READLINE)')
#     arquivo.seek(0,0)
#     print(arquivo.readline(),end='')
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
    

# print('#' * 30)
# with  open(caminho, 'r') as arquivo:
#    print(arquivo.read())
   
# o "A" escreve os arquivos sem apagar o seu arquivo anterior
with  open(caminho, 'w', encoding='utf8') as arquivo: # o "W" ele apaga todo o arquivo e escreve o que foi pedido
    arquivo.write('linha 1\n')
    arquivo.write('Atenção\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )


#os.remove(caminho)
#os.rename(caminho, 'aula116-2.txt')