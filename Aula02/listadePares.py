#Escreva um programa que recebe uma lista de números do usuário e retorna a quantidade de elementos pares prresentes na lista

numeros= input("digite uma lista de numeros separados por espaço: ").split()
numeros= [int(num) for num in numeros]

for num in numeros : 
    if num % 2 ==0:
     print(num)