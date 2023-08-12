class Pessoa:
    def __init__(pessoa,nome,idade):
        pessoa.nome = nome
        pessoa.idade = idade

    
    def imprimir_dados(indiviiduo):
        print("Nome" , indiviiduo.nome)
        print("Idade", indiviiduo.idade)

pessoa = Pessoa("Staley" , "23")
pessoa. imprimir_dados()
