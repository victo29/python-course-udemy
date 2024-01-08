"""
Shallow Copy vs Deep Copy em dados mutáveis Python
"""
import copy

d1 = {
    'c1':1,
    'c2':2,
    'l1' : [1,2,3,4,]
}  

# d2 = d1

# d2['c1'] = 1000
# print(d1)

d2 = d1.copy() #Caso o dicionario de origem contenha um dado mutavel, ele mantem o mesmo endereço na \
#memória

d2['c1'] = 1000
d2['l1'][1] = 10
print(d1)
print(d2)
d3 = copy.deepcopy(d1)
d3['l1'][1] = 20

print(20*'-')

print(d1)
print(d2)
print(d3)

