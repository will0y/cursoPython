###Calculadora
def apresentacao():
    print("##########################################\n")
    print("Bem vindo a calculadora do curso de Python\n")
    print("###########################################\n")

apresentacao()

numero1= int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:\n"))

print("Operações\n")
print("Opção 1 : ***Soma***\n")
print("Ooção 2 : ***Subtração***\n")
print("Opção 3: ***Divisão***\n")
print("Opção 4 :***Multiplicação***\n")

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicação(a,b):
    return a *b

def divisao (a,b):
    return a/b


operacao =input("Escolha uma opracao:")
num= int(operacao)
if num ==1:
    soma(numero1, numero2)
    print("O resulatdo da operacão é:")
    resultado =soma(numero1, numero2)
    print(resultado)

elif num ==2:
    subtracao(numero1, numero2)
    print("O resulatdo da operacao é: ")
    resulatdo =subtracao(numero1, numero2)
    print(resulatdo)

elif num ==3:
    divisao(numero1, numero2)
    print(" o resulatdo da operação é:")
    resulatdo =divisao(numero1, numero2)
    print(resulatdo)

elif num ==4:
    multiplicação(numero1, numero2)
    print("O resultado da oprecacao é :")
    resultado =multiplicação(numero1, numero2)
    print(resultado)


else:
    print("Operação invalida.")
    
op_soma =1
op_subtração = 2
op_divisão = 3
op_multiplicação = 4

operacao = [op_soma, op_subtração, op_divisão, op_multiplicação]

for op in operacao:
    if operacao ==1:
        print("O resultado da operação é:" )
        resulatdo =soma(numero1,numero2)







soma(numero1)
     

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicação(a,b):
    return a *b

def divisao (a,b):
    return a/b

def apresentacao():
    print("##########################################\n")
    print("Bem vindo a calculadora do curso de Python\n")
    print("###########################################\n")

