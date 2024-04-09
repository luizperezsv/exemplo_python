# Orientação a Objetos
# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print('Movimentando')
    
    def __init__(self,fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    #Setter
    def set_num_registro(selfa, registro):
        selfa.__num_registro = registro
    
    #Getter
    def get_fabr_modelo(self):
        print(f'Modelo : {self.__modelo} , Fabricante : {self.__fabricante} \n')

    def get_num_registro(self):
        return self.__num_registro

class Carro(Veiculo):
    #Método __init__ será herdado
    def movimentar(self):
        print(f'Carro se movimentando hadugen !!!!')

class Moto(Veiculo):
    def movimentar(self):
        print('Movimentar a moto inhauuuu !!!')

if __name__=='__main__':
    meu_veiculo = Veiculo('GM','Scort')
    meu_veiculo.set_num_registro(43880)
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    print(f'O veículo de número {meu_veiculo.get_num_registro()} está registrado')

    meu_carro = Carro('Honda','FIT')
    meu_carro.set_num_registro(45455)
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
    print(f'O CARRO de número {meu_carro.get_num_registro()} está registrado')

    my_moto = Moto('Yamaha','Ninja 9009')
    my_moto.set_num_registro(343)
    my_moto.movimentar()
    my_moto.get_fabr_modelo()
    print(f'A moto de número {my_moto.get_num_registro()} está registrada')