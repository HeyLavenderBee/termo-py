from tkinter import *
import random
import pandas
import numpy

app = Tk()
app.title("Termo")
app.geometry("500x500")
app.configure(background="#dde")
chute = ""
entry_str = StringVar()
response = StringVar()
letra1 = StringVar()
letra2 = StringVar()
letra3 = StringVar()
letra4 = StringVar()
letra5 = StringVar()

palavras = []
palavra_escolhida = ""

Label(app, text="Bem-vindo ao Termo em Python!",background = "#dde",foreground="#009",anchor=W).place(x=10, y=10,width=200,height=20)
entry = Entry(app, textvariable=entry_str)
entry.place(x=10,y=40,width=200,height=40)
button = Button(app,text="Adicionar palavra")
button.place(x=10,y=90)
result_label = Label(app, text="a",background = "#dde",textvariable=response).place(x=10,y=120)

main_frame = Frame(app, padx=30,pady=30,bg="#dde")
main_frame.place(x=20,y=150,width=190,height=300)

label1 = Label(main_frame, background="gray",textvariable=letra1)
label1.place(width=25,height=25,anchor="center")
label2 = Label(main_frame, background="gray",textvariable=letra2)
label2.place(x=30,width=25,height=25,anchor="center")
label3 = Label(main_frame, background="gray",textvariable=letra3)
label3.place(x=60,width=25,height=25,anchor="center")
label4 = Label(main_frame, background="gray",textvariable=letra4)
label4.place(x=90,width=25,height=25,anchor="center")
label5 = Label(main_frame, background="gray",textvariable=letra5)
label5.place(x=120,width=25,height=25,anchor="center")

def read_words_from_csv():
    df = pandas.read_csv("words.csv", usecols=["PALAVRA"])
    data_array = df.to_numpy()
    print(data_array)
    i = 0
    for data in data_array:
        data = str(data).replace("['","")
        data = data.replace("']","")
        data = data.upper()
        palavras.append(data)
        i += 1
    global palavra_escolhida
    print(palavras)
    palavra_escolhida = palavras[random.randint(0, len(palavras)-1)]
    print("Entre um total de: ",i,"itens, a palavra é: ",palavra_escolhida)
    
read_words_from_csv()

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
        response.set("O chute deve conter 5 letras")
        return
    
    entry_str.set("")
    letra1.set(chute[0])
    letra2.set(chute[1])
    letra3.set(chute[2])
    letra4.set(chute[3])
    letra5.set(chute[4])
    
    if chute == palavra_escolhida:
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
                change_label_bgcolor_yellow(i)
                if palavra_escolhida[i] == letra:
                    change_label_bgcolor_green(i)
            else:
                change_label_bgcolor_gray(i)
            i += 1
        response.set("Continue tentando.")
        chute = ""

button.config(command=checar_chute)
app.mainloop()



