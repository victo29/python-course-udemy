lista_de_tarefas = []
desfeitos = []


def listar(lista):
    print('\nTAREFAS:')
    if lista:
        for i in lista:
            print(i.upper())
    else:
        print('\nNADA A LISTAR!\n')

def desfazer(lista_de_tarefas,desfeitos):

    if not lista_de_tarefas:
        print('\nNADA A SER DESFEITO!\n')
        return

    desfeitos.append(lista_de_tarefas[-1])
    lista_de_tarefas.pop()
    listar(lista_de_tarefas)

def refazer(lista_de_tarefas, desfeitos):
    if not desfeitos:
        print('\nNADA A REFAZER!\n')
        return

    lista_de_tarefas.append(desfeitos[0])
    desfeitos.pop(0)
    listar(lista_de_tarefas)

def main():
    while True:
        tarefa_comando = input("""Comandos: listar, desfazer, refazer
Digite uma tarefa ou comando: """)

        if tarefa_comando == 'listar':
            listar(lista_de_tarefas)
        elif tarefa_comando == 'desfazer': 
            desfazer(lista_de_tarefas,desfeitos)
        elif tarefa_comando == 'refazer':
            refazer(lista_de_tarefas,desfeitos)
        else:
            lista_de_tarefas.append(tarefa_comando)

main()    