numero = int(input(" Digite um nímero:"))

if numero %5 ==0 :
    print(" Esse número é multiplo de 5.")
elif (numero %2 ==0):
    print ( " Esse número é multiplo de 2.")
elif ( numero % 3 ==0):
    print( " Esse número é multiplo de 3 ")
elif ( numero %7 ==0):
    print ( "Esse número é multiplo de 7. ")
else:
    print ( " Esse número não é multiplo de nenhum número.")