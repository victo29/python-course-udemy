# Atributo de classe
# ANO_ATUAL = 2024
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 1
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
# Pessoa.ano_atual = 1

p1 = Pessoa('Victor', 12)
p2 = Pessoa('Iasmin', 13)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(Pessoa.ano_atual)