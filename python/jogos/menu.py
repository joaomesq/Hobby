import forca
import jogo_adivinha

print("***********************************")
print("************MENU JOGO**************")
print("***********************************")

print("\n1. Adivinhação")
print("2. Forca")
escolha = int(input("Qual jogo vai ser? Digite um número: "))

if(escolha == 2):
    forca.jogar()
elif escolha == 1:
    jogo_adivinha.jogar()