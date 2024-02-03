#For dentro de For

lista =[
    (x,y)
    for x in range(3)
    for y in range(3)
]


lista =[
    [letra for letra in 'Victor']
    for x in range(3)
]

print(lista)