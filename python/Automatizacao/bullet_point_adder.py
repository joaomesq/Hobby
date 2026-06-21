#!/usr/bin/env python3
#bullet_point_adder - adiconar marcadores da wikpedia a um texto
#copiado do clipboard

import pyperclip

text = pyperclip.paste()

lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = f"* {lines[i]}"

text = "\n".join(lines)

pyperclip.copy(text)
print(pyperclip.paste())#não precisa
