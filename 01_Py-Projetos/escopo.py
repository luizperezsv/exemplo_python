# Escopo Global e Local

var_global = 'Curso'

def escreve_texto():
    global var_global
    var_global = 'Curso22'
    var_local = 'MyName'
    print(f'Var Global: {var_global}')
    print(f'Var Local: {var_local}')

if __name__ == '__main__':
    print('Executar a função escreve_texto()')
    escreve_texto()

    print('Acessar as variaveis diretamente')
    print(f'Var Global: {var_global}')
    # print(f'Var Local: {var_local}')