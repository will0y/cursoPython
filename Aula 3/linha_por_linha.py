def ler_arquivo_linha_por_linha():
    nome_arquivo = "exemplo.txt"

    # Abre o arquivo no modo de leitura ('r')
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            print(linha.strip())  #strip() remove espacos e quebras de linhas adicionais

if __name__ == "__main__":
   ler_arquivo_linha_por_linha()