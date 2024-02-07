# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Victor', 17)

p1.__dict__['nome'] = 'Iasmin'
# del p1.__dict__['idade']
p1.__dict__
print(p1.__dict__)
print(vars(p1))

dados = {'nome':'Roberto', 'idade':1}
p1 = Pessoa(**dados)

