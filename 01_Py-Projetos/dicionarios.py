#Dicionario

elemento = {
    'Z':3,
    'nome':'Lítio',
    'grupo':'Metais Alcalinos',
    'densidade':0.534
}


print('elemento: ' +  elemento['nome'])
print('densidade: ' +  str(elemento['densidade']))
print(f'O dicionario possui {len(elemento)} elementos')

# # Atualizar uma entrada

# elemento['grupo'] = 'Alcalinos'

# #Adicionar uma entrada
# elemento['periodo'] = 11
# print(elemento)

# #Excluir itens
# del elemento['periodo'] 
# print(elemento)

# elemento.clear()
# print(elemento)

for i,g in elemento.items():
    print(f'{i}: {g}')