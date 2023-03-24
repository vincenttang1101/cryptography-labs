def Encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if "A"<=char<="Z":
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        elif "a"<=char<="z":
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def Decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if "A"<=char<="Z":
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        elif "a"<=char<="z":
            plaintext += chr((ord(char) - key - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

def main():
    string = input("Enter string: ")
    key    = int(input("Enter key: "))
    E      = Encrypt(string,key)
    print("Encrypt is:", E)
    print("Decrypt is:", Decrypt(E, key))
main()
