# (Parte1) try e except para tratar exceções
try:
    a = 18
    b = 0
    print(b[0])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print('Dividiu por zero.')
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError,IndexError) as error:
    print('typeError, IndexError')
    print('ERROR:',error)
    print('NAME:',error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')
