import random

def jogar():
    print("jogo de adivinha")

    n_secreto = random.randint(1,100)
    contador_erro = 1


    for contador_erro in range (1,11) :
        
        print("Palpite n° ",contador_erro)
        palpite = float(input("Digite um número entre 1 e 100: "))

        if((palpite>100) or (palpite<1)):
            print("Você digitou um palpite inválido")
            continue
            #break

        if(palpite == n_secreto):
            print ("você acertou")
            break
        else:

            if(palpite > n_secreto):

                print("Você errou! O número secreto é menor")
        
            else:
                print("Você errou! O número secreto é maior")

        
    if((palpite>100) or (palpite<1)):
        print("Você digitou um palpite inválido")

    else:


        if(contador_erro<10):

            print("Você acertou o número")
            print("gastou ", contador_erro," chance(s)")
        else:

            print("Você esgotou as suas 10 chances")

    print(n_secreto)


if(__name__=='__main__'):
    jogar()

    
'''while(contador_erro<6) :

    print("Palpite n° ",contador_erro)
    palpite = float(input("Digite um número: "))

    print(palpite, ", esse é o meu palpite!")

    if(palpite == n_secreto):
        print ("você acertou")
        break
    else:

         if(palpite > n_secreto):

            print("Você errou! O número secreto é menor")
     
         else:
            print("Você errou! O número secreto é maior")

    contador_erro+=1


if(contador_erro<5):
    print("Você acertou o número")
    print("gastou ", contador_erro," chances")
else:
    print("Você esgotou as suas 5 chances")'''

          


'''igual = (palpite == n_secreto)
#maior = (palpite > n_secreto)


if(igual):
   print ("você acertou")
else:
   if(maior):
       print("Você errou! O número secreto é menor")
     
    else:
        print("Você errou! O número secreto é maior")'''