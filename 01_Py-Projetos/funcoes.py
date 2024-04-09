#Funções
#Modularização, Reuso de Código, Legibilidade

def mensagem():
    print('Analista Shima')
    print('Prefeitura Municipal de São Vicente')

mensagem()

#Função com argumentos
def soma(a,b):
    print(a+b)

soma(22,88)

def Mult(x, y):
    return x*y
print('O resultado de Mult é ' + str(Mult(8,88)))

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x**2)
#     return quadrados

def contar(num=11, caractere='+'):
    for i in range(0,num):
        print(caractere)

if __name__ == '__main__':
    contar(caractere='¨%',num=3)