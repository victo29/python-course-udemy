# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções

""" Decoradores são usados para fazer o Python
 usar as funções decoradoras em outras funções."""

# Decoradores são "Syntax Sugar" (Açúcar sintático)

def create_function(func):
    def internal_function(*args ,**kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        return result
    return internal_function

@create_function
def reverse_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param,str):
        raise TypeError("'param' must be a string")
    

rve = reverse_string(123)
print(rve) 