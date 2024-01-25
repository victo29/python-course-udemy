from itertools import count
#count é um iterador sem fim

c1 = count() #stap/passo
c2 = count(start= 8,step= 16)



for i in c1:
    if i > 100:
        break
    print(i)

for i in range(10):
    print(i)