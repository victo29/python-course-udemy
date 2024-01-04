def mutiplicadora(multiplicador):
    def calcular(num):
        return num * multiplicador
    return calcular

duplicar = mutiplicadora(2)
triplicar = mutiplicadora(3)
quadruplicar = mutiplicadora(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))