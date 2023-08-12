class Retangulo:
    def __init__(retangulo, altura,largura):
        retangulo.altura = altura
        retangulo.largura = largura
    
    def imprimir_dados(retangulo):
        print("base" , retangulo.altura)
        print("Altura",retangulo.largura)

    def calcula_area_retangulo(triangulo):
        base = int(input("Digite a base do triangulo"))
        largura = int(input("Digite a largura do triangulo"))
        print("A área do triangulo ","é", base*largura)
     
    
medida = Retangulo(5,5)
medida.imprimir_dados()

medida.calcula_area_retangulo()
medida.calcula_area_retangulo()


        