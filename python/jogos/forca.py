import random

def mensagem_de_abertura():
    print("***************************************")
    print("***   Bem vindo ao joga da Forca    ***")
    print("***************************************")

#pegar palavra secreta
def gerar_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for palavra in arquivo:
        palavras.append(palavra.strip())
    
    palavra_da_vez = random.randrange(0, len(palavras))
    
    return palavras[palavra_da_vez]

def inicializar_letras_acertadas(secret_word):
    return ['_' for letra in secret_word]

def pede_chute():
    chute = input("Qual letra?: ")
    return chute.strip().lower()

def marca_acerto(letras_acertadas, secret_word, chute):
    posicao = 0

    for letra in secret_word:
        if( letra.strip().lower() == chute):
            letras_acertadas[posicao] = chute
            
        posicao += 1
    
    return letras_acertadas

def mensagem_vencedor():
    print("Você ganhou!")

def mensagem_perdedor():
    print("Você perdeu!")


def jogar():
    mensagem_de_abertura()
    
    secret_word = gerar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(secret_word)
    erros = 0
    acertou = False
    enforcou = False
    
        
    print(letras_acertadas)
    while(not acertou and not enforcou):
        chute = pede_chute()
        
        if(chute.lower() in secret_word.lower()):
            letras_acertadas = marca_acerto(chute = chute, secret_word = secret_word, letras_acertadas = letras_acertadas)
        else:
            erros += 1
        
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)

    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor()