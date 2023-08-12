class Carro:
    def __init__(carro,marca,modelo,ano):
        carro.marca = marca
        carro.modelo = modelo
        carro.ano = ano
        
    def imprimir_dados(automovél):
        print("A marca do carro é ",  automovél.marca)
        print("modelo", automovél.modelo)
        print("Ano", automovél.ano)
      
    
cacchorro01 = Carro("porsche","kn", 2023) 
cacchorro01.imprimir_dados()