class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
class Carro:
    def __init__(self):
        self.habilitacao = "carro"
        
    def tipo_habilitacao(self):
        print(self.habilitacao)
        
class Moto:
    def __init__(self):
        self.habilitacao = "Moto"
        
    def tipo_habilitacao(self):
        print(self.habilitacao)
        
        

