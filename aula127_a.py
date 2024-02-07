# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def salvar_dados(self):
        with open('aula127.json', 'w',encoding='utf8') as arquivo:
            json.dump(self.__dict__, arquivo, ensure_ascii=False, indent=2)
    
    def recupera_atributos( caminho_do_arquivo):
        with open(caminho_do_arquivo,'r', encoding='utf8') as arquivo:
            pessoa = json.load(arquivo)
        return pessoa

pessoa1 = Pessoa('Victor', 17)
pessoa1.salvar_dados()