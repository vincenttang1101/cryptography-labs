import numpy as np
import random
import math
def extended_euclidean(a, b):
  mod =  b
  if b == 0:
      print(a,1,0)
      return
  x1,x2,y1,y2 = 0,1,1,0
  while b>0:
     q = a//b
     r = a-q*b
     x = x2 - q*x1
     y = y2- q*y1
     a,b,x2,y2,x1,y1 = b,r,x1,y1,x,y
  return x2%mod if x2<0 else x2

def generate_a_comma(N):
  a_comma = []
  for i in range(0, N):
    a_comma.append(sum(a_comma) + random.randint(1,5))
  return a_comma

def generate_m(generate_a_comma):
    bc = sum(generate_a_comma)
    bcd = [bc, random.randint(1,5)]
    return sum([sum(generate_a_comma), random.randint(1,5)])

def generate_w(generate_m):
    w = 2;
    while(math.gcd(w, generate_m) != 1):
        w+=1
    return w;

def generate_plaintext(a_comma):
    plaintext_binary = ""
    for i in range(len(a_comma)):
        temp = str(random.randint(0, 1))
        plaintext_binary += temp
    return(plaintext_binary)
 
def a_comma(N):
    a_comma = list(map(int,input("\nEnter the numbers : ").strip().split()))[:N]
    return a_comma

def trapdoor_knapsack_encode(plain_text, a, m):
    split_plaintext = [plain_text[i:i+1] for i in range(0, len(plain_text), 1)]
    convert_plaintext_int = [int(abc) for abc in split_plaintext]
    cipher_text = sum(np.multiply(convert_plaintext_int, a).tolist())%m
    fcipher_text = open("ciphertext.txt", "w")
    fcipher_text.write(str(cipher_text))
    print("Encode: "+str(cipher_text))
    return cipher_text

def trapdoor_knapsack_decode(cipher_text, w_inverse, m, a_comma):
    T_comma = cipher_text*w_inverse%m
    size_a_comma = len(a_comma)
    x = ''
    for i in a_comma:
        size_a_comma -= 1
        if (T_comma >= a_comma[size_a_comma]):
            x+=str(1)
            T_comma = T_comma-a_comma[size_a_comma]*1
        else:
            x+=str(0)
    print("Decode: "+str(x[::-1]))
    return x[::-1] 
            
    
def main():
    N = int(input("Enter the length of N: "))
    super_increasing = generate_a_comma(N)
    m = generate_m(super_increasing)
    w = generate_w(m)
    w_inverse = extended_euclidean(w, m)
    a = np.multiply(super_increasing, w).tolist()
    print("<--------------------Merkle–Hellman knapsack cryptosystem--------------------!>")
    print("Data after generating: a="+str(super_increasing)+", N="+str(N)+", m="+str(m)+", w="+str(w)+", w_inverse="+str(w_inverse))
    print("Public key "+str(a))
    print("Private key "+str(super_increasing)+" "+str(m)+"|"+str(w))
    
    fpublic_key = open("public_key.txt", "w")
    fpublic_key.write(str(a))
    fprivate_key = open("private_key.txt", "w")
    writea = fprivate_key.write(str(super_increasing)+" "+str(m)+"|"+str(w))
    fplain_text_1 = open("plain_text.txt", "w+")
    abcd = fplain_text_1.write(str(generate_plaintext(super_increasing)))
    fplain_text_1.close()
    fplain_text_2 = open("plain_text.txt", "r")
    read_plain_text = fplain_text_2.read()
    print("Plain text: "+str(read_plain_text))
    
    trapdoor_knapsack_encoded = trapdoor_knapsack_encode(read_plain_text, a, m)
    decode = trapdoor_knapsack_decode(trapdoor_knapsack_encoded, w_inverse, m, super_increasing)
    ascii_string = "".join([chr(int(binary, 2)) for binary in decode.split(" ")])
    print("The message after being converted from binary->ASCII:", ascii_string)
    print("<----------------------------------------------------------------------------!>")
    print("All information about the trapdoor knapsack cipher is saved at:")
    print("1. Public key is saved at public_key.txt\n2. Private key is saved at private_key.txt\n3. Encryption is saved at cipher.txt\n4. Decryption is saved at plain_text.txt")
    
main()
