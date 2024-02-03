# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def create_function(func):
    def internal_function(*args ,**kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return internal_function

def reverse_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param,str):
        raise TypeError("'param' must be a string")
    

reverse_strings_checking_the_params = create_function(reverse_string)
print(reverse_strings_checking_the_params('123'))