
def return_sum(list_a,list_b):
    small_list = min(list_a,list_b)
    return [ list_a[i]+list_b[i] for i in range(len(small_list))]

list_a = [1,2,3,4,5,6,7]
list_b = [1,2,3,4]

result = return_sum(list_a,list_b)
print(result)

lista_soma = [x + y for x,y in zip(list_a,list_b)]
print(lista_soma)