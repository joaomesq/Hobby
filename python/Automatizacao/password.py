#!/usr/bin/env python3
# Um programa para repositórios de senha, não seguro ainda.

import sys, pyperclip

PASSWORDS = {
    'email': "Joaob.mesquita1@gmail.com", 'blog': 'cafeDigita', 'luggage': '1234',
    'test@example.com': "password"
}

if(len(sys.argv) < 2):
    print('Usage: python password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]# primeiro argumento é o nome da conta

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    senha = pyperclip.paste()
    print(f"Password for {account} copy to clipboard")
else:
    print(f"There is no account named {account}")
    