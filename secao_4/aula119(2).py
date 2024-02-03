import json
import sys

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


def ler(tarefas, caminho_do_arquivo):
    dados = []
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_do_arquivo)
    return dados
        

def salvar(tarefa, caminho_do_arquivo):
    with open(caminho_do_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefa, arquivo, indent=2,ensure_ascii=False)
    return dados

CAMINHO_DO_ARQUIVO = 'aula119.json'
lista_de_tarefas = ler([],CAMINHO_DO_ARQUIVO)
desfeitos = []


def main():
    while True:
        tarefa_comando = input("""Comandos: listar, desfazer, refazer
Digite uma tarefa ou comando: """)
        
        comandos = {
            'listar': lambda: listar(lista_de_tarefas),
            'desfazer': lambda: desfazer(lista_de_tarefas,desfeitos),
            'refazer': lambda: refazer(lista_de_tarefas,desfeitos),
            'parar': lambda: sys.exit(),
            'adicionar': lambda: adicionar(tarefa_comando,lista_de_tarefas)
        }

        comando = comandos.get(tarefa_comando)  if comandos.get(tarefa_comando) is not None \
        else comandos['adicionar'] 
        comando()
        salvar(lista_de_tarefas,CAMINHO_DO_ARQUIVO)
main() 