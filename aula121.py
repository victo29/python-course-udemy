# Métodos em instâncias de classes Python
# Self é o mesmo que o objeto fora da classe
# Hard coded - É algo que foi escrito
# Classe é o molde e NÃO tem dados
# Na Classe o self é a própria instância

class Carro:
    def __init__(self, nome='tanto faz'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

print('-'*30)

celta = Carro(nome= 'Celta')
print(celta.nome)

