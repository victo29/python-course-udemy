def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica






print(
    executa(
        lambda x, y: x + y,  #Função soma  
        3,4
        
    )
)

duplica = executa(
    lambda m : lambda n: n*m,  #Função  cria_multiplicador
       2   
)

print(duplica(3))


print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8,9
    )
)