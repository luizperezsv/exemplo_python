#Recursividade

# Fórmula geral para o fatorial:
# fatorial(num) = 1, se num = 0 ou se num = 1
# fatorial(num) = num * fatorial(num - 1), para num > 1
# 4! -> 4 * fat(3) = 4 * 3 * fat(2) = 4 * 3 * 2 * 1 = 24

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    x = int(input('Digite um número inteiro positivo para calcutar o seu fatorial : '))
    fat = fatorial(x)
    print(f'O fatorial de {x} é {fat}')     
