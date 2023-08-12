class Triângulo:
    def __init__(triangulo,base,altura):
        triangulo.base = base
        triangulo.altura = altura

    def imprimir_dados(triangulo):
       print("base" , triangulo.base)
       print("Altura", triangulo.altura)

    def calcula_area_triangulo(triangulo):
        base = int(input("Digite a base do triangulo"))
        altura = int(input("Digite a altura do triangulo"))
        print("A área do triangulo " "é", base*altura/2)
     
    
medida = Triângulo(5,4)
medida.imprimir_dados()

medida.calcula_area_triangulo()
medida.calcula_area_triangulo()






