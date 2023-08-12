from tkinter import*

janela = Tk()
janela.title("Formulario de cadastro")
janela.geometry("400x400+400+100")
janela.config(bg = "blue")
janela.resizable(0,0)

#Texto de entrada
txtEbtrada = Entry(janela,text="",width=20, font ="arial")
txtEbtrada.place(x=50, y= 100)

#Funçãp de verificação
def verificar():
    numero =int (txtEbtrada.get())

    if numero % 2 ==0  and numero !=0:
        Iblesultado["text"] = "Esse numero é par"
    elif (numero %2