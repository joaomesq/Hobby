import random

secret_number = random.randint(1, 20);

print("Estou pensando em um número qualquer, tente adivinhar: ")

for pensando_em in range(1, 7):
    print("Tentativa numero {}\n".format(pensando_em))
    chute = int(input())

    if(type(chute) != int):
        print("Chute precisa ser um número inteiro")
        continue

    if chute > secret_number:
        print("Ups! Número maior que o número que estou pensando")
    elif chute < secret_number:
        print("Ups! Chute menor que número secreto")
    else:
        break# chute == secret_ number

if(chute == secret_number):
    print("Parabens")
else:
    print("Perdeu!")