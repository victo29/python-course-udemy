# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# - o set aceitam tuplas pois são imutáveis

s1 = {1,2,3,3,3,3,3,3,3,4,5,5,5,5,} #Eliminam valores duplicados
print(s1)

l1 = [1,2,3,3,3,3,3,3,3,4,5,5,5,5]
s2 = set(l1)
l1 = list(s2)
print(l1)