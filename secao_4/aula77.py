# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]



for i in range(3):
    dicionario = perguntas[i]
    print(dicionario['Pergunta'])
    
    for indicie,valor in enumerate(dicionario['Opções']):
        print(f'{indicie}) {valor}')
    resposta = int(input('->'))
    
    if dicionario['Opções'][resposta] == dicionario['Resposta']:
        print('Prabéns vc acertou!')
    else:
        print('Vicê errou!')