class Cachorro:
    def __init__(cachorro,nome,idade):
        cachorro.nome = nome
        cachorro.idade = idade
        
    def imprimir_dados(cachorro):
        print("Nome", cachorro.nome)
        print("Idade", cachorro.idade)
      
    
cacchorro01 = Cachorro("Caramelo",6 )
cacchorro01.imprimir_dados()