file_name = input("Type file name: ")

try:
    file = open(file_name)
except:
    print(f"File cannot be opened: {file_name}")
    exit()

def write():
    for line in file:
        print(line.upper())

def find_spam():
    count = 0
    total = 0

    for line in file:
        start_word = "X-DSPAM-Confidence: 0.8475"
        if not line.startswith(start_word): continue

        size = len(start_word)
        word = line[:size]
        indice = word.find("0")
        number = float(word[indice:])

        count = count + 1
        total = total + number

    print(f"Média de confiança de spam:{total} {count} {total/count}")

find_spam()