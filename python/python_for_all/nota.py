try:
    nota = float(input("Digite a pontuação: "))
    if(nota >= 1 or nota <= 0):
        print("Pontuação Inválida!")
    elif(nota >= 0.9):
        print("A")
    elif(nota >= 0.8):
        print("B")
    elif(nota >= 0.7):
        print("C")
    elif(nota >= 0.6):
        print("D")
    elif(nota < 0.6):
        print("D")
    
except:
    print("Erro! Digite entrada numerica")