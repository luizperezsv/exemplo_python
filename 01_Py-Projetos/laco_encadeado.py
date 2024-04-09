import random

# for cont_ex in range(1,7):
#     print(f'\nRodada: {cont_ex}')
#     for cont_in in range(8,0, -2):
#         print(f'\nValor: {cont_in}')

# print('FIM')

soma = 0
# for a in range(1,10):
#     print(f'\Conjunto {a}')
#     # for b in range(10):
#     num = random.randint(1000,9999)
#     soma = soma + num
#     print(f'Valor: {num}')
# print('Valor Final é ' + str(soma))
numNotMatBas = random.randint(15,30)
numNotMatEsp = random.randint(20,40)
soma = numNotMatBas+numNotMatEsp

print(f'Nota da matéria Básica é de {numNotMatBas}. \n')
print(f'Nota da matéria Específica é de {numNotMatEsp}. \n')
strSoma = str(soma)
print(f'A nota final de José Ricardo Oshiro Shimabukuro é de {soma}. \n')

