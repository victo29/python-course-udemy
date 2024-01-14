# dir, hasattr e getattr em Python

string = 'Victor'
metodo = 'upper'
if hasattr(string, metodo):
    print('possui uppeer')
    print(getattr(string,metodo)())
    print(string.upper())