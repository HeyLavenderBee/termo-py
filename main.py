from tkinter import *
import random
import pandas
import numpy

app = Tk()
app.title("Termo")
app.geometry("500x500")
app.configure(background="#dde")
chute = ""
tentativas = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
cur_round = 0
entry_str = StringVar()
response = StringVar()
letra1 = StringVar()
letra2 = StringVar()
letra3 = StringVar()
letra4 = StringVar()
letra5 = StringVar()

globals()["letras1"] = letra1

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

posy = 30
def create_line(colors):
    posx = 0
    global posy
    global cur_round
    for i in range(5):
        Label(main_frame, background=colors[i],text=tentativas[cur_round][i]).place(x=posx,y=posy,width=25,height=25,anchor="center")
        posx += 30
    posy += 30
    cur_round += 1
    posx = 0

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

def end_game():
    print(f"Você alcançou o limite de tentativas, a palavra era: {palavra_escolhida}")

def checar_chute():
    global chute
    global cur_round
    chute = entry.get()
    chute = chute.upper()
    
    if cur_round >= 6:
        end_game()
        return
    
    #primeiro verifica se o chute tem 5 letras
    if len(chute) != 5:
        response.set("O chute deve conter 5 letras")
        return
    
    entry_str.set("")

    if chute == palavra_escolhida:
        response.set(f"Parabéns, você acertou! A palavra era: {palavra_escolhida}.")
        for letra in chute:
            tentativas[cur_round] += letra
        create_line(["green", "green", "green", "green", "green"])
    else:
        i = 0
        colors = []
        for letra in chute:
            tentativas[cur_round] += letra
            if letra in palavra_escolhida:
                if palavra_escolhida[i] == letra:
                    colors.append("green")
                else:
                    colors.append("yellow")
            else:
                colors.append("gray")
            i += 1
        print(colors)
        create_line(colors)
        colors = []
        response.set("Continue tentando.")
        chute = ""

button.config(command=checar_chute)
app.mainloop()



