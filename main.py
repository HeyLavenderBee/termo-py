from tkinter import *
import random

app = Tk()
app.title("Termo")
app.geometry("500x500")
app.configure(background="#dde")
chute = ""
response = StringVar()
letra1 = StringVar()
letra2 = StringVar()
letra3 = StringVar()
letra4 = StringVar()
letra5 = StringVar()

palavras = ["PARDO","BARCO","VERDE","ANZOL","LABIO","PUNIR","CASAL","PULSO","FALSO","PILHA","CACHO","ZEBRA","FERRO","PRETO","PEITO","UNIAO","CURVA","SUBIR","CORDA","BRACO","SAMBA","NATAL","CARRO","MEDIA","MEDIR","BOMBA"]
palavra_escolhida = palavras[random.randint(0, len(palavras)-1)]

Label(app, text="Bem-vindo ao Termo em Python!",background = "#dde",foreground="#009",anchor=W).place(x=10, y=10,width=200,height=20)
entry = Entry(app)
entry.place(x=10,y=40,width=200,height=40)
button = Button(app,text="Me clique!")
button.place(x=10,y=90)
result_label = Label(app, text="a",background = "#dde",textvariable=response).place(x=10,y=120)

label1 = Label(app, background="gray",textvariable=letra1)
label1.place(x=20,y=220,width=25,height=25,anchor="center")
label2 = Label(app, background="gray",textvariable=letra2)
label2.place(x=50,y=220,width=25,height=25,anchor="center")
label3 = Label(app, background="gray",textvariable=letra3)
label3.place(x=80,y=220,width=25,height=25,anchor="center")
label4 = Label(app, background="gray",textvariable=letra4)
label4.place(x=110,y=220,width=25,height=25,anchor="center")
label5 = Label(app, background="gray",textvariable=letra5)
label5.place(x=140,y=220,width=25,height=25,anchor="center")

def change_label_bgcolor_green(n):
    n += 1
    if n == 1:
        label1.config(background="green")
    elif n == 2:
        label2.config(background="green")
    elif n == 3:
        label3.config(background="green")
    elif n == 4:
        label4.config(background="green")
    elif n == 5:
        label5.config(background="green")

def change_label_bgcolor_yellow(n):
    n += 1
    if n == 1:
        label1.config(background="yellow")
    elif n == 2:
        label2.config(background="yellow")
    elif n == 3:
        label3.config(background="yellow")
    elif n == 4:
        label4.config(background="yellow")
    elif n == 5:
        label5.config(background="yellow")

def change_label_bgcolor_gray(n):
    n += 1
    if n == 1:
        label1.config(background="gray")
    elif n == 2:
        label2.config(background="gray")
    elif n == 3:
        label3.config(background="gray")
    elif n == 4:
        label4.config(background="gray")
    elif n == 5:
        label5.config(background="gray")

def checar_chute():
    global chute
    chute = entry.get()
    chute = chute.upper()
    
    #primeiro verifica se o chute tem 5 letras
    if len(chute) != 5:
        print("O chute deve conter 5 letras.")
        response.set("O chute deve conter 5 letras")
        return
    
    letra1.set(chute[0])
    letra2.set(chute[1])
    letra3.set(chute[2])
    letra4.set(chute[3])
    letra5.set(chute[4])
    
    if chute == palavra_escolhida:
        print(f"Parabéns, você acertou! A palavra era: {palavra_escolhida}.")
        response.set(f"Parabéns, você acertou! A palavra era: {palavra_escolhida}.")
        change_label_bgcolor_green(0)
        change_label_bgcolor_green(1)
        change_label_bgcolor_green(2)
        change_label_bgcolor_green(3)
        change_label_bgcolor_green(4)
    else:
        i = 0
        for letra in chute:
            if letra in palavra_escolhida:
                print(f"A letra {letra} está na palavra.")
                change_label_bgcolor_yellow(i)
                if palavra_escolhida[i] == letra:
                    change_label_bgcolor_green(i)
            else:
                print(f"A letra {letra} não está na palavra.")
                change_label_bgcolor_gray(i)
            i += 1
        print("Continue tentando.")
        response.set("Continue tentando.")
        chute = ""

button.config(command=checar_chute)
app.mainloop()


