# Tudo em python é um objeto
a = 'A'
b = 'B'
c = 1.1
formato = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c) #parametro nomeado

print(formato)
