# Escopo da Classe e de métodos da Classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def alimentando(self, alimento):
        print(f'{self.nome} está se alimentando de {alimento} ')

    def executar(self, *args):
        return self.alimentando(args)

leao = Animal(nome='Leão')
print(leao.nome)
# leao.alimentando('carne')
leao.executar('Carne','Frango','Bufalo')
