# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


def generator(n=0):

    yield 1 #pausa
    print('Continuando.........')
    yield 2
    print('Continuando.........')
    yield 3
    return 'Acaba aqui'

gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)



def generator_1(n=0, maximum=10):
    while True:
        yield n
        n+=1
        if n > maximum:
            return 'ACABOU'

gen_1= generator_1()
for n in gen_1:
    print(n)