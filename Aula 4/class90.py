class Animal:
    def __init__(self, nome, tipo,som):
        self.nome = nome
        self.tipo = tipo
        self.som = som

    def imprimeDados(self):
        print(" o nome do cachorro é:", self.nome)
        print(" o tipo de animal é:" , self.tipo)
        print(" o som que ele emite é: ", self.som)
    
    
    
    def emiteSom(sellf):
        print("O animal emite o som", sellf.som)

cachorro = Animal("Rex", "canino" ,"auau")

cachorro.imprimeDados()
cachorro.emiteSom()

