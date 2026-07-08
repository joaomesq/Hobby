#!/usr/bin/env python3

import re, pyperclip

phone_regex = re.compile(r'''(
        ((\+|\+\s)?\d{3}|\((\+|\+\s)?\d{3}\))? #indicador
        (\s|-|\.)? #separador
        (\d{3}) #primeiros três digitos
        (\s|-|\.)? #separador
        (\d{3}) #primeiros três digitos
        (\s|-|\.)? #separador
        (\d{3}) #primeiros três digitos
)''', re.VERBOSE|re.DOTALL)

email_regex = re.compile(r'''(
            [a-zA-Z0-9.+%_]+   #nome do usuário
            @                   #simbolo @
            [a-zA-Z0-9.-]+      #dominio
            (\.[a-zA-Z]{2,})              
)''', re.VERBOSE|re.DOTALL)


text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_number = "-".join([groups[5], groups[7], groups[9]])
    
    matches.append(phone_number)

for groups in email_regex.findall(text):
    email = groups[0]
    matches.append(email)


if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard")
    print("\n".join(matches))
else:
    print("No Number or email found")
