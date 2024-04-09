#Trocar o valor entre duas variáveis

var1=44
var2=78

# print(f'Var1 = {var1} e Var2 = {var2}' )

# var2,var1 = var1, var2 

# print(f'Var1 = {var1} e Var2 = {var2}' )

# Operador Condicional Ternário

# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')
# print(f'Menor valor é {(var1,var2)[var1>var2]}')

# Generator

# valores = [1,2,3,4,5,7,8,9,10]
# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valor in quadrados :
#     print(valor)

# Enumerate()
# bebidas = ['café', 'chá','agua', 'suco', 'refri']

# for i, item in enumerate(bebidas):
#     print(f'Indice: {i}, Item: {item}')

# Gerenciamento de contexto com with

with open('frutas.txt','r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')