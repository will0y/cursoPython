class Veiculo:
  def __init__(self, velocidade, cor, modelo, marca):
        self.velocidade = velocidade
        self.cor = cor
        self.modelo = modelo
        self.marca = marca


  def imprimir_dados(Automovel):
      print("A velocidade do carro é", Automovel.velocidade)
      print("A cor do carro é", Automovel.cor)
      print("O modelo do carro é", Automovel.modelo)
      print("A marca do carro é", Automovel.marca)

    
class Carro(Veiculo):
    def __init__(self, velocidade, cor, modelo, marca):
        super().__init__(velocidade, cor, modelo, marca)
        self.marca =marca

    def ligar(veículo):
        print("Carro ligado")

carro1 =Carro("veloz","preto", "kn" , "porsch")
carro1.ligar()



    
