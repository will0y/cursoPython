class  Veiculo:
     def __init__(self,veiculo,velocidade):
          self.veiculo = veiculo
          self.velocidade = velocidade

     def acelerar(self):
          print("Veiculo acelerou")

class Carro(Veiculo):
     def __init__(self, veiculo, velocidade, marca):
          self.marca = marca
          return super().__init_veiculo, velocidade

def ligar(self):
          print("o carro ligou")

meuCarro = Carro("Carro" ,"10_km",  "Ford")

meuCarro.ligar()
meuCarro.acelerar() 