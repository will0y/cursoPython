contatos = ()


def adcionar(): 
     nome = input("Digite seu nome ")
     telefone = input (" Digite um telefone,", sep=-"-")
     email = input ("Digite seu email ")
     contatos[nome] = {"telefone": telefone, "email": email}
     print("Conato adicionado com sucesso!/n")
   

def visualizar():
    if contatos:
     for nome , valor in contatos():
         print("nome:", nome)
         print("telefone", valor["telefone"])
         print("Email", valor["email"])
         print("-----------------------------")

def atualizar(): 
     nome = input("Digite o nome do conato que você deseja atualizar:")
     if nome in contatos:
         telefone = input("Digite o novo telefone:")
         email = input("Digite o novo email:")
         contatos[nome]["telefone'"] = telefone
         conatatos[nome]["email"] = email
         print("Contato atualizado com sucesso")
     else:
         print("Contato não encontrado")
     
     
def excluir_contato():
    nome =  input("Digite o nome do conato que deseja excluir:")
    if nome in contatos:
        del contatos[nome]
        print(" Contato excluido com sucesso!")
    else:
        print("Contato não econtrado.")




    








