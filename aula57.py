salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    #['Luiz', 'João', 'Eduarda', (0,10,20) ]
    ['Luiz', 'João', 'Eduarda' ],  # 2
]

#print(salas[2][3][2])

for sala in salas:
    print(f'A sala é{sala}')
    for aluno in sala:
        print(aluno)