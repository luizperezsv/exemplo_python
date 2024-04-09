import random

print('Gerar 6 números aleatórios\n')
# for i in range(6):
#     n = random.randint(1,99)
#     print(f'Número gerado: {n}')

# valor = random.random()
# print(round(valor * 10,2))

# valor = random.uniform(1,100)
# print(round(valor,1))

L = [1,3,5,7,9,34,67,79,88]
# n = random.choice(L)
# print(f'Número sorteado: {n}')

# n = random.sample(L,3)
# print(f'Número sorteado: {n}')

#Embaralhar 

print(f'Exibir a lista na ordem original: {L}')
print('Embaralhar a lista e exibi-la : ')
n = random.shuffle(L)
print(L)
