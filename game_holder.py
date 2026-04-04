from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
import pandas
import random

guess = ""
guess_list = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
words = []
chosen_word = ""

class Letter(QLabel):
    def __init__ (self, letter, color):
        super().__init__()
        self.letter = letter
        self.color = color
        self.setText(self.letter)
        self.setStyleSheet(f"background-color: {self.color}; padding: auto")

    def change_status(self, passed_color, passed_letter):
        self.color = passed_color
        self.letter = passed_letter
        self.setStyleSheet(f"background-color: {self.color}; padding: auto")
        print("Color changed!")

class ButtonHolder(QWidget):
    def __init__ (self):
        super().__init__()

        cur_round = 0

        letter_test = Letter("A", "green")

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

        def change_label_color(colors):
            letter_row = QHBoxLayout()
            for letter in guess:
                label = Letter(letter, "gray")
                letter_row.addWidget(label)
            widget.addLayout(letter_row) #adds row to screen
            letter1.setStyleSheet(f"background-color:{colors[0]}; padding: auto")
            letter2.setStyleSheet(f"background-color:{colors[1]}; padding: auto")
            letter3.setStyleSheet(f"background-color:{colors[2]}; padding: auto")
            letter4.setStyleSheet(f"background-color:{colors[3]}; padding: auto")
            letter5.setStyleSheet(f"background-color:{colors[4]}; padding: auto")
            #testing letter class to change this function later
            letter_test.change_status(colors[0], "R")

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
                color_array = []
                i = 0
                for letter in guess:
                    if letter in chosen_word:
                        if guess[i] == chosen_word[i]:
                            color_array.append("green")
                        else:
                            color_array.append("#e8aa25")
                    else:
                        color_array.append("gray")
                    i += 1
                change_label_color(color_array)
                if input.text().upper() == chosen_word:
                    guess_label.setText("Parabéns!")

        self.resize(600,500)
        self.setWindowTitle("Termo em Python")
        title = QLabel("Bem-vindo ao Termo em Python!")
        title.setStyleSheet("font-size: 20px;")
        input = QLineEdit("")
        input.setStyleSheet("padding: 7px; font-size: 14px")
        button = QPushButton("Adicionar palavra")
        button.setGeometry(100,100,100,100)
        button.clicked.connect(check_word)

        guess_label = QLabel("")

        letter_gray = "background-color: gray; padding: auto"

        letter1 = QLabel("A")
        letter1.setStyleSheet(letter_gray)
        letter2 = QLabel("B")
        letter2.setStyleSheet(letter_gray)
        letter3 = QLabel("C")
        letter3.setStyleSheet(letter_gray)
        letter4 = QLabel("D")
        letter4.setStyleSheet(letter_gray)
        letter5 = QLabel("E")
        letter5.setStyleSheet(letter_gray)

        letter_row = QHBoxLayout()
        letter_row.addWidget(letter1)
        letter_row.addWidget(letter2)
        letter_row.addWidget(letter3)
        letter_row.addWidget(letter4)
        letter_row.addWidget(letter5)

        widget = QVBoxLayout()
        #widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        widget.addWidget(input)
        widget.addWidget(button)
        widget.addWidget(guess_label)
        widget.addWidget(letter_test)
        widget.addLayout(letter_row)
        self.setLayout(widget)

