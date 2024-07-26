# Utilizando Setter
# getter -> Obter valor

# -> Convenção para sinalizar atributos protegidos _atributo ou __atributio

class Caneta:
    def __init__(self,cor):
        # self._cor = cor; # -> Convenção para sinalizar atributos protegidos _atributo ou __atributio
        self.cor = cor # Utilizando o setter já no init para caso tenham condições que são de execução obritória

    @property # -> Faz com que um método se comporte igual um atributo
    def cor(self):
        print("Something before");
        return self._cor;

    @cor.setter # -> Definindo o setter do atributo protegido
    def cor(self, cor):
        # Pode conter restições antes da definição do atributo
        self._cor = cor;


caneta = Caneta('Azul');

caneta.cor = 'Rosa';

print(caneta.cor)

