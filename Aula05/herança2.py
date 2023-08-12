class veiculo:
    
    def __init__(veiculo, marca, modelo, cor):
        veiculo.marca = marca
        veiculo.modelo = modelo
        veiculo. cor =cor

    def imprimir_dados(veiculo):
        print(" a marca deese veiculo é: ", veiculo.marca)
        print(" o modelo dessse veiculo é", veiculo.modelo)
        print("a cor desse veiculo é:", veiculo.cor)

    def aceleraveiculo(veiculo):

        print(" o veiculo acelerou, bibi")

meuVeiculo =veiculo("Infinit", "250", "Cinza ")

meuVeiculo.imprimir_dados()
meuVeiculo.aceleraveiculo()