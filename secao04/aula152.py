def error_zero_division(n):
    if n == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return True

def divide(n, d):
    error_zero_division(d)
    return n / d

print(divide(2, 4))
print(divide(2, 0))
