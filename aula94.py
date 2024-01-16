try:
    print('Open')
    print(8/0)
except ZeroDivisionError:
    print('you tried division a number by zero, this is not possible')
else:
    print('there were no errors')
finally:
    print('Close')
