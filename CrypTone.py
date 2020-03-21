# Eren Car - https://github.com/erencar

import base64

def bs64_encode(text):      # base64 encode

    print(base64.b64encode(text.encode('utf-8')).decode('utf-8'))

def bs64_decode(text):      # base64 decode
    try:
        print(base64.b64decode(text.encode('utf-8')).decode('utf-8'))

    except UnicodeDecodeError:
        print("Please Enter Valid String for Base64 !!!")


def ceaser_encry(text, shift):   # Ceaser Encode
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    print(cipher)

def ceaser_decry(message):   # Ceaser Decode
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(26):
        for letter in message:
            if letter in alpha:
                letter_index = (alpha.find(letter) - i) % len(alpha)
                result = result + alpha[letter_index]
            else:
                result = result + letter
        print(i," = ",result)
        result=""


def vigenere_encry(text, key):
    keylen = len(key)
    key = key.upper()
    key_int = [ord(i) for i in key]
    text_int = [ord(i) for i in text]
    ciphertext = ''
    for i in range(len(text_int)):
        value = (text_int[i] + key_int[i % keylen]) % 26
        ciphertext += chr(value + 65)
    print(ciphertext)

def vigenere_decry(text, key):
    keylen = len(key)
    key = key.upper()
    key_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in text]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_int[i % keylen]) % 26
        plaintext += chr(value + 65)
    print(plaintext)

# --------------------------- Main -----------------------------------#

print("----- Welcome the CrypTone ----- \n")

while True:
    print("Please Select the Number")
    print("1- Encode-Encrypt \n"+"2- Decode-Decrypt\n"+"0- Exit")
    try:
        numinput = int(input())
        if numinput == 1:
            print("1- Base64\n"+"2- Ceaser\n"+"3- Vigenere\n"+"00- Back the Main Menu ")
            encryinput = int(input())

            if encryinput == 1:
                text=input("Please Enter String = ")
                bs64_encode(text)

            elif encryinput == 2:
                print("Alpha = ABCDEFGHIJKLMNOPQRSTUVWXYZ \n")
                text = input("Enter string: ")
                shift = int(input("Enter Shift Number: "))
                ceaser_encry(text, shift)

            elif encryinput == 3:
                print("Alpha = ABCDEFGHIJKLMNOPQRSTUVWXYZ \n")
                text = input("Enter Text: ")
                key = input("Enter Key : ")
                vigenere_encry(text, key)

            elif encryinput == 00:
                continue

        elif numinput == 2:
            print("1- Base64\n" + "2- Ceaser\n" + "3- Vigenere\n"+"00- Back the Main Menu ")
            decryinput = int(input())

            if decryinput == 1:
                text = input("Please Enter String = ")
                bs64_decode(text)

            elif decryinput == 2:
                print("Alpha = ABCDEFGHIJKLMNOPQRSTUVWXYZ \n")
                text = input("Enter string: ")
                ceaser_decry(text)

            elif decryinput == 3:
                print("Alpha = ABCDEFGHIJKLMNOPQRSTUVWXYZ \n")
                text = input("Enter Text: ")
                key = input("Enter Key : ")
                vigenere_decry(text, key)

            elif decryinput == 00:
                continue

        elif numinput == 0:
            print("----- Thanks For Using -----\n"+"https://github.com/erencar\n"+"https://erencar.com.tr")
            break
            
    except ValueError:
        print("!!! Integer Please !!!\n")
