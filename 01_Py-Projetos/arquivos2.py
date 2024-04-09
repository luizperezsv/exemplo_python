# try:
#     manipulador = open('aqui.txt', 'a', encoding='utf-8')
#     manipulador.write('\nShima começou a trabalhar ma prefeitura dia 09/12/2022 \n')
#     manipulador.write('No mesmo dia em que o Brasil foi eliminado pela Croácia.')
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

frutas = ['Morango\n','Amora\n','Uva\n','Carambola\n','Laranja\n']

try:
    manipulador = open('frutas.txt','w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print('Arquivo problemático')
else:
    manipulador.close()   

try:
    manipulador = open('frutas.txt','r', encoding='utf-8')   
    print(manipulador.read()) 
except IOError:
    print('Arquivo problemático')
else:
    manipulador.close()     