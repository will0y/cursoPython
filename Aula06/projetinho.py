class CadastroPessoas:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self,pessoa):
        self.pessoas.append(pessoa)

    def exibir_pessoas(self):
        for pessoa in self.pessoas:
            print(f"nome: {pessoa.nome}, Idade: {pessoa.idade}, Email: {pessoa.Email}")
        
    



    




































"""self.nome = nome
        self.idade = idade

    def imprimir_dados(pessoa):
        print("o nome da pessoa é", pessoa.nome)
        print("A idade é", pessoa.idade)"""