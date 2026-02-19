from tkinter import *
import random

app = Tk()
app.title("Termo")
app.geometry("500x500")
app.configure(background="#dde")
chute = "BARCO"

def checar_chute():
    global chute
    print(chute)
    #primeiro verifica se o chute tem 5 letras
    if len(chute) != 5:
        print("O chute deve conter 5 letras.")
    
    if chute == palavra_escolhida:
        print(f"Parabéns, você acertou! A palavra era: {palavra_escolhida}.")
    else:
        for letra in chute:
            if letra in palavra_escolhida:
                print(f"A letra {letra} está na palavra.")
            else:
                print(f"A letra {letra} não está na palavra.")
        print("Continue tentando.")
        chute = ""

Label(app, text="Bem-vindo ao Termo em Python!",background = "#dde",foreground="#009",anchor=W).place(x=10, y=10,width=200,height=20)
input_t = Entry(app)
input_t.place(x=10,y=40,width=200,height=40)
button = Button(app,text="Me clique!")
button.place(x=10,y=90)
button.config(command=checar_chute)

palavras = ["PARDO","BARCO","VERDE","ANZOL","LABIO","PUNIR","CASAL","PULSO","FALSO","PILHA","CACHO","ZEBRA","FERRO","PRETO"]
palavra_escolhida = palavras[random.randint(0, len(palavras)-1)]
app.mainloop()


