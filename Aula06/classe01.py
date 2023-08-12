class Cliente:
    def __init__(cliente,nome):
        cliente.nome = nome
        
    def imprimir_dados(cliente):
        print("Nome", cliente.nome)
      
    
cliente01 = Cliente("Wiilian")
Cliente.imprimir_dados(cliente01)
