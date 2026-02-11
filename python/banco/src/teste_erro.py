from conta import ContaCorrente

def metodo1():
    print("Inicio metodo 1")
    metodo2()
    print("Fim metodo 1")

def metodo2():
    print("Inicio metodo 2")
    cc = ContaCorrente(saldo = 1200, numero = 1, titular = "Mesquita")
    for i in range(1, 15):
        cc.deposita(i + 100)
        print(cc.extrato())
        if i == 5:
            cc = None

        
    
    print("Fim metodo 2")


if __name__ == "__main__":
    print("Inicio main")
    try:
        metodo1()
    except:
        print("Erro")
    print("Fim main")