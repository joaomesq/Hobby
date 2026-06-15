def collatz(number):
    if(number % 2 == 0):
        return number // 2
    else:
        return (3 * number + 1)
    

try:
    number = int(input("Insira o número: "))
except ValueError:
    print("Insira um número inteiro");

while True:
    number = collatz(number)
    print(number)
    if(number == 1):
        break