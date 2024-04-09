#Manipulação de arquivos de texto

# manipulador = open('aqui.txt', 'r', encoding='utf-8')

# print(f'\Método read():\n')
# print(manipulador.read())

# print(f'\Método readline():\n')
# print(manipulador.readline())

# print(f'\Método readlines():\n')
# print(manipulador.readlines())

try:
    manipulador = open('aqui.txt', 'r', encoding='utf-8')
   # manipulador = open('C:\\Users\\joseshimabukuro\\Documents\\Transcrição áudio 7.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()