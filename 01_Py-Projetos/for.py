# lista = [12,34,56,79,88,100]

# for item in lista:
#     print(item)

# palavra = 'Paralelepípedo'

# for letra in palavra:
#     print(letra)

# for numero in range(5,11):
#     print(numero)

# nome = input('Digite o seu nome: ')

# for x in range(22):
#     print(f'{x+1} {nome}')

#range(valor_inicial, valor_final, incremento)

for x in range(100,2,-2):
    print(x)

pedras = ('Rubi','Esmeralda','Diamante','Quartzo','Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)
