lista = [12, -2, 4,	8,	29,	45,	78,	36,	-17, 2,	12,	8, 3, 3, -52]
maior = lista[0]
menor = lista[0]
pares = []
total_ocorrencia_primeiro_elemento = 0
total = 0
soma_valores_negativos = 0

for value in lista:
    #Maior - Menor
    if(value < maior):
        maior = value
    elif(menor > value):
        menor = value
    
    #pares
    if(value % 2 == 0):
        pares.append(value)
    
    #ocorrências primeiro elemento
    if(value == lista[0]):
        total_ocorrencia_primeiro_elemento += 1
    
    #media
    total += value

    #valoes negativos
    if(value < 0):
        soma_valores_negativos += value
    
media = total/len(lista)


print("Lista:\nMaior: {}\nMenor: {}".format(maior, menor))
print("Pares: {}".format(pares))
print("Total Ocorrência primeiro elemento: {}".format(total_ocorrencia_primeiro_elemento))
print("Media: {}".format(total))
print("Soma valoes negativos: {}".format(soma_valores_negativos))