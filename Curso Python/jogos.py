#jogos.py

import forca
import jogoAdivinha

def escolher_jogo():

    print("*************")
    print("bem-vindo ao jogo")

    print("Para joga a forca digite (1), para jogar adivinhação digite (2) ")


    jogo = int(input("Qual jogo você jogará? "))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    if(jogo == 2):
        print("jogando adivinhação")
        jogoAdivinha.jogar()

if(__name__=='__main__'):
    escolher_jogo()