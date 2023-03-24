import string
FILTER_CHAR = 'X'
cipher_text_vigenere = 'FDKKQFUDKJQQ'
plain_text_vigenere  = 'DAIHOCSAIGON'
keyword_playfair = 'MONARCHY'
plain_text_playfair = 'balloon'


def findKey(plain_text,cipher_text):
  key=''
  format_key = ''
  final_key=''
  
  for i in range (0,len(plain_text)):
      key+= chr(((ord(cipher_text[i].upper()) - ord(plain_text[i].upper())) % 26)+65)
  print(key)
  for k in key:
    final_key+=k
    if(vigenere_encode(plain_text,final_key)==cipher_text.upper()):
      return final_key

def vigenere_encode(plaintext,keyword):
  result = ""
  round_key = list(ord(k)-65 for k in keyword.upper())
  for index,char in enumerate(plaintext.upper()):
    ascii_code = ord(char)
    if ascii_code in range(65,91):
      result += chr((round_key[index % len(keyword)] + ascii_code-65) % 26  + 65)
    else:
      result+=char
  return result 

def create_matrix(key):
  i=0
  key=key.replace(" ","")
  key = key.upper()
  key = key.replace("J","I") #Convert J to I
  matrix = ''
  for ch in key:
    if ch not in matrix:
        matrix+=ch
  for ch in string.ascii_uppercase:
    if ch not in key and ch!='J':
      matrix+=ch
  return matrix
def format_text(plain_text):
  plain_text = plain_text.replace(" ","")
  plain_text_as_array = list(plain_text)
  plain_text_as_pair = []
  while plain_text_as_array:
    if(len(plain_text_as_array) >= 2):
      l,r = [plain_text_as_array.pop(0) for i in range(2)]
      if(l==r):
        plain_text_as_array.insert(0,r)
        r=FILTER_CHAR
      plain_text_as_pair.append(l+r)
    else:
      plain_text_as_pair.append(plain_text_as_array.pop(0)+FILTER_CHAR)        
  return plain_text_as_pair
def playfair_encode(pair,matrix):
  a,b=list(pair)
  coor_a,coor_b = matrix.find(a),matrix.find(b)
  col_a,col_b = coor_a % 5, coor_b % 5
  row_a,row_b = coor_a // 5, coor_b // 5
  new_coor_a,new_coor_b=0,0
  if(col_a == col_b):
    new_coor_a = (coor_a+5) % 25
    new_coor_b = (coor_b+5) % 25
  elif(row_a == row_b):
    new_coor_a = row_a*5+((coor_a +1) % 5)
    new_coor_b = row_b*5 +((coor_b +1) % 5)
  else:
    new_coor_a = (coor_b % 5) + row_a * 5
    new_coor_b = (coor_a % 5) + row_b  * 5
  return matrix[new_coor_a]+matrix[new_coor_b]
def playfair_decode(pair,matrix):
  a,b=list(pair)
  coor_a,coor_b = matrix.find(a),matrix.find(b)
  col_a,col_b = coor_a % 5, coor_b % 5
  row_a,row_b = coor_a // 5, coor_b // 5
  new_coor_a,new_coor_b=0,0
  if(col_a == col_b):
    new_coor_a = (coor_a-5) % 25
    new_coor_b = (coor_b-5) % 25
  elif(row_a == row_b):
    new_coor_a = row_a*5+((coor_a -1) % 5)
    new_coor_b = row_b*5 +((coor_b -1) % 5)
  else:
    new_coor_a = (coor_b % 5) + row_a * 5
    new_coor_b = (coor_a % 5) + row_b  * 5
  return matrix[new_coor_a]+matrix[new_coor_b]
def playfair_decoding(cipher_text,key):
  matrix = create_matrix(key)
  plain_text = ''
  cipher_text = cipher_text.upper()
  cipher_text = format_text(cipher_text)
  for pair in cipher_text:
    plain_text+=playfair_decode(pair,matrix)
    
  return plain_text   
def playfair_encoding(plain_text,key):
  matrix = create_matrix(key)
  cipher_text = ''
  plain_text = plain_text.upper()
  plain_text = format_text(plain_text)
  for pair in plain_text:
    cipher_text+=playfair_encode(pair,matrix)
    
  return(cipher_text)
print("=====================\nFIND KEY VIGENERE")

print("KEY IS:",findKey(plain_text_vigenere,cipher_text_vigenere))
cipher_text_playfair = playfair_encoding(plain_text_playfair,keyword_playfair)
decoded_text_playfair = playfair_decoding(cipher_text_playfair,keyword_playfair)


print("=====================\nPLAYFAIR CIPHER")
print('Plain text:',plain_text_playfair)
print("Cipher text:",cipher_text_playfair)
print("Decoded text:",decoded_text_playfair)
