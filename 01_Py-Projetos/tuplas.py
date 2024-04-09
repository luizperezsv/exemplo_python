#São imutáveis

halogenios = ('F','Cl','Br','I','At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
print(elementos)


t1 =(1,1,3,3,5,77,99,55,88,1,1,4,5,7,99)
print(t1.count(886))
print(elementos[1])

for elemento in elementos:
    print(f'Elemento : {elemento}')