class Pessoa:
    def _init_(pessoa,nome,idade, e_mail, endereço):
        pessoa.nome = nome
        pessoa.idade = idade
        pessoa.e_mail = e_mail
        pessoa.endereço = endereço
        

    def imprimir_dados(pessoa):
        print("Nome:", pessoa.nome)
        print("Idade:", pessoa.idade)
        print("e_mail:", pessoa. e_mail)
        print("Endereço:", pessoa.endereço)


#Teste do exercicio
pessoa = Pessoa("Cassio", 38,'cassio.matematica@gmail.com', "Alto da mocca")
Pessoa.imprimir_dados()  #Saida: Nome: João  

