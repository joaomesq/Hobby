#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print(f"Precisas inserir um número e só um numero para ser verificado")
    sys.exit()

def verify_phone_number(text):
    if(len(text) < 12 or len(text) > 12):
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-' or text[7] != '-':
        return False
    
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True

if(len(sys.argv[1]) > 12):
    message = sys.argv[1]
    for i in range(len(message)):
        chunck = message[i:i+12]
        if(verify_phone_number(chunck)):
            print(f"Phone number found: {chunck}")
else:
    print(verify_phone_number(sys.argv[1]))

print("Done!")
