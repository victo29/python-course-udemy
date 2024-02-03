#Escopo de funções e módulos em Python + global
x=1
def escopo():
    global x
    x = 2
    z = 10
    def outra_func():
        x=11
        y=2
        print(x,y,z)
    outra_func()
    print(x,z)

print(x)
escopo()
print(x)