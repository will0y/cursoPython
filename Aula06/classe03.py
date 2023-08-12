class Conta_banacaria:
    def __init__(conta_bancaria,titular,saldo):
        conta_bancaria.titular = titular
        conta_bancaria.saldo = saldo
        

    def depositar (conta_bancaria, valor):
        conta_bancaria += valor

    def sacar(conta_bancaria,valor):
        if valor <= conta_bancaria.saldo:
            conta_bancaria -= valor
        else:
            print("Saldo insuficiente")

    def imprimir_saldo(conta_bancaria):
        print("Saldo:'", conta_bancaria.saldo)


conta =("João")
conta.depositar(100)
conta.sacar(50)
conta.imprimir_saldo()
    
