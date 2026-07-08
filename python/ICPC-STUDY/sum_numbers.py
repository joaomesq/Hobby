'''t = int(input())

for _ in range(t):
    numbers = input().strip()
    
    print(sum(map(int, numbers)))
'''
'''
numbers = input().strip()
numbers = list(map(int, numbers.split()))
t = int(input())


for _ in range(t):
    q = input().split()
    if(q[0] == "Q"):
        print(sum(numbers[int(q[1]) - 1:int(q[2])]))
    else:
        i = int(q[1]) - 1
        numbers[i] =int(q[2])
'''
'''
n = int(input().strip())

for _ in range(n):
    a, b = input().split()
    
    a = int(a[::-1])
    b = int(b[::-1])

    print(int(str(a+b)[::-1]))
'''
'''
while True:
    a, b, c = map(int, input().split())

    if  a == 0 and b == 0 and c == 0:
        break

    if c - b == b - a:
        d = c - b
        print(f"PA: {c+d}")
    elif (c / b) == (b / a):
        r = c // b
        print(f"PG: {c*r}")
'''
'''
t = int(input().strip())
import math

for _ in range(t):
    n = int(input().strip())
    print(math.factorial(n))
'''
'''
ano = int(input().strip())

while True:
    ano = ano + 1 
    if len(set(str(ano))) == 4:
        print(ano)
        break
'''
'''
t = int(input().strip())

for _ in range(t):
    h, min = map(int, input().split())

    min_dia = 24 * 60
    min_atual = h * 60 + min
    print(f"{min_dia - min_atual}")
'''
'''
t = int(input().strip())
for _ in range(t):
    a, b = map(int, input().split("+"))
    print(a + b)
'''
'''
t = int(input().strip())

for _ in range(t):
    n_legs = int(input().strip())

    vacas = n_legs // 4
    legs_restantes = n_legs - vacas * 4
    galinhas = legs_restantes // 2

    print(galinhas + vacas)
'''
'''
name_user = input().strip()

gender = set(name_user)
if len(gender) % 2 == 0:
    print("CHAT WITH HER")
else:
    print("IGNORE HIM!")
'''
'''
n = int(input().strip())
x = 0

for _ in range(n):
    command = input().strip()
    if "++" in command:
        x += 1
    elif "--" in command:
        x -= 1

print(x)
'''
'''
word = input().strip()
print(word[0].upper()+word[1:])
'''

'''
a, b = map(int, input().split())

if a + b == a * b:
    print("YES")
else:
    print("NO")
'''
'''
n = int(input().strip())
numbers = list(map(int, input().split()))

min_val = min(numbers)
n_operacoes = max(0, -min_val)

if min_val < 0:
    numbers = [x + n_operacoes for x in numbers]

n_operacoes += numbers[0]

for i in range(1, n):
    d = numbers[i] - numbers[i-1]
    if d > 0:
        n_operacoes += d

print(n_operacoes)
'''

'''
t = int(input())

for _ in range(t):
    x = int(input().strip())
    x_binary = bin(x >> 1)
    
    count_1 = x_binary.count('1')

    ultimo_bit = x & 1

    if count_1 % 2 != ultimo_bit:
        print("-1")
    else:
        print(count_1)
'''

def f(n):

    if n <= 0: return 0
    if n<= 1: return 1

    anterior = 0
    atual = 1

    for _ in range(2, n +1):
        next = anterior + atual

        anterior = atual
        atual = next

    return atual
    
print(f(4))