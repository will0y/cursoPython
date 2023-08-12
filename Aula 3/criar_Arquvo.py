def criar_arquivo():
    nome_arquivo = "exemplo.odt"

    #Abre o arquivo no modo de escrita('w')
    with open(nome_arquivo,"w") as arquivo:
        arquivo.write("Este é um exemplo de arquivo criado com Pyhton.\n")
        arquivo.write("Você pode escrever várias linhas neste arquivo.\n")

if __name__ == "__main__":
    criar_arquivo()