import os 

os.chdir('C:\\Shima_Python_Learning\\01_Py-Projetos\\teste')
print(f'Diretório atual : {os.getcwd()}' )

padrao_nome = input('Qual o padrão de nome dos arquivos a usar ?')

for cnt, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, ext_arq = os.path.splitext(arq)
        if cnt < 10:
            nome_arq = padrao_nome + ' 0' + str(cnt)
        else:    
            nome_arq = padrao_nome + ' ' + str(cnt)
        nome_novo = f'{nome_arq}{ext_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados.')