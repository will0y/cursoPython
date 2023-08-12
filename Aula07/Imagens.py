import tkinter as tk
from PIL import Image, ImageTk

def main():
    janela = tk.Tk()
    janela.title("Exemplo de inserção de imagem")

    #Carregando a imagem usando a biblioteca PIL (Pyhton Imaging Library)
    image = Image.open("santos.png")
    photo = ImageTk.PhotoImage(image)

    #Criando um rótulo para exibir a imagem
    label = tk.Label(janela, image)
    label.pack()

    janela.mainloop()

    if __name__ == "__main__":
        main()

    #Criando um rótulo para exibir a Imagem
