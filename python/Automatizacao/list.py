def listToString(lista):
    if(len(lista) == 0):
        return ""
    
    if(len(lista) == 2):
        return f"{lista[0]} an {lista[1]}"
    
    if(len(lista) == 1):
        return str(lista[0])

    
    itens_iniciais = ", ".join(lista)
    
    return f"{itens_iniciais} and {str(lista[-1])}"

print(listToString(["bana", "aplle", "orange", "tomato"]))