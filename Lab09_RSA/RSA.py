import random
import math

def sieve_of_eratosthenes():
    n = random.randint(3, 1000)
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, math.isqrt(n)+1):
        if (is_prime[i]):
            for j in range(i*i, n, i):
                is_prime[j] = False
    return [i for i in range(n) if (is_prime[i])]

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

def fast_modular_exponentiation(a, n, m):
    r = 1
    while(n > 0 ):
        if(n % 2 == 1):
            r =(r * a) % m
        a = (a * a) % m
        n //= 2
    return r

def main():
    while True:     
        print("\n######################Menu công việc hệ mã RSA######################\nTiến trình chọn công việc để thực hiện hệ mật mã RSA:")
        print("Chọn công việc:\n● Tạo khoá (K)\n● Xác thực (A)\n● Bảo mật (C)\n● Thoát ra ngoài HT(X)")
        option = input("Chọn: ")
        if (option == "K"):
            eratos = sieve_of_eratosthenes()
            choose_2_primes = random.sample(eratos,2)
            p = choose_2_primes[0]
            q = choose_2_primes[1]
            print("\n######################Khởi tạo khoá######################\nTiến trình tạo khoá:")
            print("Chọn ngẫu nhiên 2 số nguyên tố trong sàng nguyên tố: p="+str(p)+", q="+str(q))
            ϕn = (p-1)*(q-1)
            n = p*q
            print("n =", n)
            print("ϕn = (p-1)(q-1) =", ϕn)
            print("1. Nhập khoá e:\n2. Sinh khoá e:")
            option_e = int(input("Chọn: "))
            if (option_e == 1):
                e = int(input("Nhập: "))
                if (math.gcd(e, ϕn) == 1 and e != 1):
                    e
                else:
                    print("Khoá e không có nguyên tố cùng nhau với ϕn")
            elif (option_e == 2):
                while True:
                    e = random.randint(2, ϕn-1)
                    if (math.gcd(ϕn, e) == 1):
                        e
                        break;
            d = extended_euclidean(e, ϕn)
            print("e =", str(e)+", d = "+str(d))
            print("Khoá công khai: (n, e) = ("+str(n)+", "+str(e)+")")
            print("Khoá bí mật: (p, q, d) = ("+str(p)+", "+str(q)+", "+str(d)+")")
        elif (option == "A"):
            print("\n######################Giải mã######################\nTiến trình chọn Xác thực để thực hiện công việc giải mã:")
            ciphertext = encrypt
            decrypt = fast_modular_exponentiation(ciphertext, d, n)
            print("Bản rõ:", decrypt)
        elif (option == "C"):
            print("\n######################Mã hoá######################\nTiến trình chọn Bảo mật để thực hiện công việc mã hoá:")
            plaintext = int(input("Nhập bản rõ: "))
            if (plaintext < n):
                e = int(input("Nhập khoá e: "))
                encrypt = fast_modular_exponentiation(plaintext, e, n)
                print("Bản mã:", encrypt)
        elif (option == "X"):
            exit()
main()
