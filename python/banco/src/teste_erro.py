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
    '''
    print("Inicio main")
    try:
        n = 2
        n = n / 1
        print("Nenhum erro")
        #metodo1()
    except (ZeroDivisionError, AttributeError):
        print("Erro!")
    else:
        print("Talvez apreendas de verdade")
    
    print("Fim main")
    try:
        #n = 2 / 0
        raise NameError('oi')
    except:
        print("Lançou um excepção")
        #raise
    '''
    def divisao(x, y):
        '''try:
            resultado = x / y
        except ZeroDivisionError:
            print("Divisão por Zero")
        else:
            print("Resultado {}".format(resultado))
        finally:
            print("Executando o finally!")
        '''
        if(x > y):
            raise ValueError("x maior que y")
        
        print("Não para a execução")

    divisao(5, 1) 