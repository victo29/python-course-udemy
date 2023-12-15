#Como funciona o for por debaixo dos panos

# texto = iter('Victor') # __iter__()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))
#print(texto.__next__())

texto = 'Victor'
iterador = iter(texto)
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break