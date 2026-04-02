from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QStyle
import pandas
import random

guess = ""
guess_list = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
words = []
chosen_word = ""

class ButtonHolder(QWidget):
    def __init__ (self):
        super().__init__()

        cur_round = 0

        def read_words_from_csv():
            df = pandas.read_csv("words.csv", usecols=["PALAVRA"])
            data_array = df.to_numpy()
            i = 0
            for data in data_array:
                data = str(data).replace("['","")
                data = data.replace("']","")
                data = data.upper()
                words.append(data)
                i += 1
            global chosen_word
            chosen_word = words[random.randint(0, len(words)-1)]
            print("Entre um total de: ",i,"itens, a palavra é: ", chosen_word)
        
        read_words_from_csv()

        def end_game():
            print(f"Você alcançou o limite de tentativas, a palavra era: {chosen_word}")
            guess_label.setText(f"Você alcançou o limite de tentativas, a palavra era: {chosen_word}")

        def check_word():
            guess = input.text().upper()
            if cur_round > 5:
                print(cur_round)
                end_game()
            if len(guess) != 5:
                print(len(guess))
                print("A palavra precisa ter 5 letras!")
            else:
                guess_label.setText(input.text())
                guess_label.adjustSize()
                input.setText("")
                letter1.setText(guess[0])
                letter2.setText(guess[1])
                letter3.setText(guess[2])
                letter4.setText(guess[3])
                letter5.setText(guess[4])
                if input.text().upper() == chosen_word:
                    guess_label.setText("Parabéns!")

        self.resize(600,500)
        self.setWindowTitle("Termo em Python")
        label = QLabel("Bem-vindo ao Termo em Python!")
        input = QLineEdit("")
        button = QPushButton("Adicionar palavra")
        button.setGeometry(100,100,100,100)
        button.clicked.connect(check_word)

        guess_label = QLabel("")

        letter_style = "background-color: gray; padding: auto"

        letter1 = QLabel("A")
        letter1.setStyleSheet(letter_style)
        letter2 = QLabel("B")
        letter2.setStyleSheet(letter_style)
        letter3 = QLabel("C")
        letter3.setStyleSheet(letter_style)
        letter4 = QLabel("D")
        letter4.setStyleSheet(letter_style)
        letter5 = QLabel("E")
        letter5.setStyleSheet(letter_style)

        letter_row = QHBoxLayout()
        letter_row.addWidget(letter1)
        letter_row.addWidget(letter2)
        letter_row.addWidget(letter3)
        letter_row.addWidget(letter4)
        letter_row.addWidget(letter5)

        widget = QVBoxLayout()
        widget.addWidget(label)
        widget.addWidget(input)
        widget.addWidget(button)
        widget.addWidget(guess_label)
        widget.addLayout(letter_row)
        self.setLayout(widget)

