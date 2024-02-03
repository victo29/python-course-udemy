# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


#print(123)
# raise ValueError('there was error')

# def division(a,b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('____saving the file____')

def no_accept_zero(d):
    
    if d == 0:
        raise ZeroDivisionError('you are try division by zero')
    return True

def must_be_int_or_float(num):
    type_of_num = type(num)
    if not isinstance(num,(float,int)):
        raise TypeError(
            f'{num} must be int or float'
            f'\n the value sent is a {type_of_num.__name__} '
        )
    return True

def division(n , d):

    must_be_int_or_float(d)
    must_be_int_or_float(n)

    no_accept_zero(d)





print(division(8,'0')) 
