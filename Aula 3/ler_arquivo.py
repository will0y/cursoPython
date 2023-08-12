def ler_arquivo():
    nome_arquivo = "exemplo.txt"

    #Abre o arquivo no modo de leitura ('r")
    with open(nome_arquivo,'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

if __name__ == "__main__":
    ler_arquivo()