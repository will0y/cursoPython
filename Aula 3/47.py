##Exercício 4: Verificação de existência
##Escreva um programa que declare uma tupla e verifique se um elemento específico está presente nela.


tupla =(10,20,30,40,50)
elemento = int(input("Digite um numero para eu procurar:"))
if elemento in tupla:
    print("o elemento", elemento, "está prsenete na tupla.")
else:
    print("o ellemento", elemento, "não esta presente na tupla.")
