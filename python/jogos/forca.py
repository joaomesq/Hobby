
def jogar():
    print("***************************************")
    print("***   Bem vindo ao joga da Forva    ***")
    print("***************************************")
    
    secret_word = 'banana'
    letras_acertadas = []
    erros = 0
    acertou = False
    enforcou = False
    
    #montando espaços
    while(len(secret_word) > len(letras_acertadas)):
        letras_acertadas.append("_")
        
    print(letras_acertadas)
    while(not acertou and not enforcou):
        chute = input("Qual letra?: ")
        posicao = 0
        
        if(chute.lower() in secret_word.lower()):
            for letra in secret_word:
                if(letra.lower() == chute.lower()):
                    letras_acertadas[posicao] = chute
            
                posicao += 1
        else:
            erros += 1
        
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu!")