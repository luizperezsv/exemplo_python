# Funções lambda (anônima)
#Sintaxe:
#lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(0,11):
#     print(quadrado(i))

#Função map()
#Sintaxe
#map(função, iterável)

# numero = [1,2,3,4,5,6,7,8,9]
# dobro = list(map(lambda x: x*2, numero))
# print(dobro)

# palavras = ['beta', 'gama', 'alfa','ômega', 'pegasus']
# maius = list(map(str.upper, palavras))
# print(maius)

#Função filter()
#Sintaxe
#filter(função,sequencia)

# def numeros_pares(n):
#     return n % 2 == 0
# num = [1,2,3,4,5,6,7,8,9]
# num_par = list(filter(numeros_pares, num))
# print(num_par)

# num_impar = list(filter(lambda x: x % 2 != 0, num))
# print(num_impar)

#Função reduce()
#Sintaxe
#reduce(função, sequencia, valor_inicial)

from functools import reduce

# def mult(x,y) :
#     return x*y
# numeros = [1,2,7,9]

# total = reduce(mult,numeros)
# print(total)

numeros = [1,2,4]
total = reduce(lambda x,y: x**2 + y**2, numeros)
print(total)