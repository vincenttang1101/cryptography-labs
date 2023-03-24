import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
#key = 'xnyahpogzqwbtsflrcvmuekjdi'

def Encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def Decrypt(ciphertext, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in ciphertext)

def main():
    key = input("Enter key: ")
    if (len(key) == 26):
        check = 0;
        for char in alphabet:
            count = key.count(char) 
            if (count > 1):
                print("There are duplicate characters:", char)
                check +=1
        if (check == 0):
            text = input("Enter text: ")
            print("1: Encrypt substiution cipher\n2: Decrypt substiution cipher")
            option = int(input("Enter option: "))
            if (option == 1):
                print(Encrypt(text, key,alphabet))
            elif (option == 2):
                print(Decrypt(text, key, alphabet))
            else:
                print("Invalid option !")
    else:
        print("Make sure the correct number of 26 characters")

main()
