# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2024  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    
    @classmethod
    def criar_com_80_anos(cls, nome): # Cria um novo objeto com a idade já definida, esses são os factories, eles
        return cls(nome, 80)          # criam objetos da classe, seguindo uma lógica ou parâmetro nesse caso
                                      # Serve também para acessar a classe sem a necessidade de uma instância 
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo',idade)



Pessoa.metodo_de_classe
p1 = Pessoa.criar_com_80_anos('Nelson')
print(p1.idade, p1.nome)
p2 = Pessoa.criar_sem_nome('23')
print(p2.nome,p2.idade)