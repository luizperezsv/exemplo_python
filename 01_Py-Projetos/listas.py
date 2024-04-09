#Listas representam uma sequencia de valores

#Sintaxe: nome da lista = [valores]

notas = [2,4,6,8,10]
notas2 = [1,3,5,7,9]
valores = notas + notas2 
# print(str(valores) + '\n')
# print(str(valores[3]) + '\n')
# print(str(valores[-2]) + '\n')
# print(str(valores[4:]) + '\n')
# print(str(valores[-4:]) + '\n')
# print('A variavel valores tem ' + str(len(valores)) + ' elementos')
# print('A lista em ordem crescente : ' + str(sorted(valores)))
# print('A lista em ordem decrescente : ' + str(sorted(valores, reverse=True)))
# print('A somatória dos elementos é ' + str(sum(valores)))
# print('O menor valor é ' + str(min(valores)) + ' e o maior valor é ' + str(max(valores)))

# 
# planetas = ['Mercúrio','Venus','Terra','Marte','Júpiter','Saturno','Urano','Netuno','Plutão']

# for planeta in planetas:
#     print(f'Planeta : {planeta}')
bebidas =[]
for i in range(0,5):
    bebida = input(f'Digite o nome de uma bebida ({i+1}): ')
    bebidas.append(bebida) 

bebidas = sorted(bebidas)
for bebida in bebidas:
    print(f'Bebida: {bebida}')
#print(bebidas)

