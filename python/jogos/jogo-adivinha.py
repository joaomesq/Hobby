print("***************************************")
print("*         Jogo de Adivinhação         *")
print("***************************************")

nivel = int(input("Escolha o nivél(1, 2, 3): "))

secrect_number = 21
if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
elif(nivel == 3):
    tentativas = 5
else:
    nivel = 5

for rodada in range(1, tentativas + 1):
    print("\nRodade {} de {}".format(rodada, tentativas))
    
    chute = int(input("\nDigite um número: "))
    print("Voce digitou {}\n".format(chute))

    acertou = secrect_number == chute
    maior = secrect_number < chute
    menor = secrect_number > chute
    
    if(acertou):
        print("Você acertou!")
        break
    elif(maior):
        print("Você errou! Chute maior que número secreto")
    elif(menor): 
        print("Você errou! Chute menor que número secreto")
    else:
        print("Você errou!")

print("\nFim do jogo!")