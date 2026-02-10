#import pygame
import random

palavras = ["PARDO","BARCO","VERDE","ANZOL","LABIO","PUNIR","CASAL","PULSO","FALSO","PILHA","CACHO","ZEBRA","FERRO","PRETO"]
palavra_escolhida = palavras[random.randint(0, len(palavras)-1)]
chute = ""

def main():
    print("Bem vindo ao Termo (feito em python)")
    checar_chute()

def checar_chute():
    chute = input("Digite seu chute: ")

    chute = chute.upper()
    #primeiro verifica se o chute tem 5 letras
    if len(chute) != 5:
        print("O chute deve conter 5 letras.")
        return
    
    if chute == palavra_escolhida:
        print(f"Parabéns, você acertou! A palavra era: {palavra_escolhida}.")
    else:
        for letra in chute:
            if letra in palavra_escolhida:
                print(f"A letra {letra} está na palavra.")
            else:
                print(f"A letra {letra} não está na palavra.")
        print("Continue tentando.")
        checar_chute()

main()