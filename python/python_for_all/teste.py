file_name = input("Type file name: ")

try:
    file = open(file_name)
except:
    print(f"File cannot be opened: {file_name}")
    exit()

file_out = open("out.txt", "w")

count = 0
for line in file:
    if line.lower().startswith("subject"):
        count = count + 1
        file_out.write(f"{line}\n")

file_out.close()

print(f"There were {count} Subject lines in {file_name}")
