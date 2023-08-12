8from tkinter import *
from tkinter.constants import END

janela = Tk()
janela.title("Formulario de cadastro")

#Largura x altura + distnacia margem esquerda + distancia ao topo
janela.geometry("500x500+500+200") 

#DEFININDO A COR DE FUNDO DA JANELA
janela.config(bg = "gray")

#LABELS
IBlnome = Label (janela, text = "Nome", width =8, font = "arial")
IBlnome.place(x=100, y=100)
txtNome = Entry(janela, text= "" , width = 20, font = "arial")
txtNome.place(x=200, y=100)

IblEmail = Label (janela,text= "Email", width= 8, font = "arial")
IblEmail.place(x=100, y=150)
txtEmial = Entry (janela, text="", width =20, font = "arial")
txtEmial.place(x=200, y=150)

Ibltelefone = Label (janela,text= "Email", width= 8, font = "arial")
Ibltelefone.place(x=100, y=200)
txtTelefone = Entry (janela, text="", width =20, font = "arial")
txtTelefone.place(x =200, y =200)

Iblcpf = Label (janela,text= "Email", width= 8, font = "arial")
Iblcpf.place(x=100, y=250)
txtcpf = Entry (janela, text="", width =20, font = "arial")
txtcpf.place(x =200, y =250)

#FUNÇÃO DO BOTÃO ENVIAR

def Enviar():
    
    IblResultado["text"] = "Dados Enviados com Sucesso!"
    txtNome.delete(0, END)
    txtEmial.delete(0,END)
    txtTelefone.delete(0,END)
    txtcpf.delete(0,END)

    


#botoes

btnEnviar = Button(janela, text= "Enviar", width= 20, command="", font="arial")
btnEnviar.place(x=100, y=300)

#label para exibir resultado
IblResultado = Label(janela,text= "Resultado", width= 20, font= "arial")
IblResultado.place(x=100, y=350)



janela.mainloop()





