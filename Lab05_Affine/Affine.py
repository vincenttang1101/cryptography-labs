import math

def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 

def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None 
  else: 
    return x % m 
 
def encrypt_affine(text, key): 
  #E = (a*x + b) % 26 
  return ''.join([ chr((( key[0]*(ord(t) - ord('a')) + key[1] ) % 26) + ord('a')) for t in text.lower().replace(' ', '') ]) 


def decrypt_affine(cipher, key): 
  #D(E) = (a^-1 * (E - b)) % 26
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('a') - key[1])) % 26) + ord('a')) for c in cipher ]) 


def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encrypt_vigenere(text, key): 
  encrypt_text = [] 
  for i in range(len(text)): 
    x = (ord(text[i].upper()) +ord(key[i].upper())) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text).upper()) 

def decrypt_vigenere(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i].upper()) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

  
def main():
  text = input("Enter the message: ")
  print("1: Affine cipher\n2: Vigenere cipher")
  option = int(input("Enter option: "))
  if (option == 1):
      key = []
      key = [int(item) for item in input("Enter the key : ").split()]
      if (len(key) == 2 and math.gcd(key[0], 26) == 1):
        enc_affine = encrypt_affine(text, key) 
        print('Encrypted Text:', encrypt_affine(text, key)) 
        print('Decrypted Text:', decrypt_affine(enc_affine, key))
      else:
        print("Invalid key !");
  elif (option == 2):
     keyword = input("Enter the keyword: ")
     key = generateKey(text, keyword)
     enc_vigenere = encrypt_vigenere(text, key) 
     print("Encrypted message:", enc_vigenere.lower()) 
     print("Decrypted message:", decrypt_vigenere(enc_vigenere, key).lower())
  else:
    print("Invalid option !")
main() 
