"While + While"

QUATIDADE_LINHAS = 5
QUANTIDADE_COLUNAS = 5


linha = 1
while linha <= QUATIDADE_LINHAS:
    coluna = 1
    while coluna <= QUANTIDADE_COLUNAS:
        print(f'{linha=} {coluna=}')
        coluna+=1
    linha+=1