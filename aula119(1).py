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

def adicionar(tarefa, lista_de_tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('\n você não digitou uma terefa!'.upper())
        return
    lista_de_tarefas.append(tarefa)


def main():
    while True:
        tarefa_comando = input("""Comandos: listar, desfazer, refazer
Digite uma tarefa ou comando: """)
        
        comandos = {
            'listar': lambda: listar(lista_de_tarefas),
            'desfazer': lambda: desfazer(lista_de_tarefas,desfeitos),
            'refazer': lambda: refazer(lista_de_tarefas,desfeitos),
            'adicionar': lambda: adicionar(tarefa_comando,lista_de_tarefas)
        }

        comando = comandos.get(tarefa_comando)  if comandos.get(tarefa_comando) is not None \
        else comandos['adicionar'] 
        comando()
main()   