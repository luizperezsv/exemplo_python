# Exceção é um objeto que representa um erro no programa
# Blocos try...except

n1 = 4
n2 = 2 

try:
    r = round(n1 / n2,2)
except ZeroDivisionError:
    print('Não é possível dividir por zero')
else:
    print(f'O resultado é {r}')