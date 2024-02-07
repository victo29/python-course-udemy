# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.
#Self é utilizado no Python para referenciar a própria instância de uma classe

# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self,nome,sobrenome): 
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Victor','Souza')
# p1.nome = 'Victor'
# p1.sobrenome = 'Souza'
print(p1.nome,p1.sobrenome)

p2 = Pessoa('Iasmin','Caldeira')
# p2.nome = 'Iasmin'
# p2.sobrenome = 'Caldeira'
print(p2.nome,p2.sobrenome)
