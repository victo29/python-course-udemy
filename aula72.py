def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total

def par_impar(num):
    if num % 2 == 0:
        return f"O número {num} é par"
    else:
        return f"O número {num} é ímpar"

mult = multiplica(12,10,10)
print(mult)

impar_par = par_impar(3)
print(impar_par)
