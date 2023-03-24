def extended_euclidean(a,b):
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
  return mod+x2 if  x2<0 else x2

def chinese_remainder_theorem(a1,a2,a3,m1,m2,m3):
  M1,M2,M3 = m2*m3,m1*m3,m1*m2
  y1,y2,y3 = extended_euclidean(M1,m1),extended_euclidean(M2,m2),extended_euclidean(M3,m3)
  return (a1*M1*y1 + a2*M2*y2 + a3*M3*y3) % (M1*m1)

def fast_modular_exponentiation(a, n, m):
    r = 1
    while(n > 0 ):
        if(n % 2 == 1):
            r =(r * a) % m
        a = (a * a) % m
        n //= 2
    return r

def main():
    print("1: Chinese Remainder Theorem\n2: Fast Modular Exponentiation")
    option = int(input("Enter option: "))
    if(option == 1):
        a1 = int(input("Enter a1:"))
        a2 = int(input("Enter a2:"))
        a3 = int(input("Enter a3:"))
        m1 = int(input("Enter m1:"))
        m2 = int(input("Enter m2:"))
        m3 = int(input("Enter m3:"))
        print("x =",chinese_remainder_theorem(a1,a2,a3,m1,m2,m3), "+", str(m1*m2*m3)+"k")
    elif (option == 2):
        a = int(input("Enter a: "))
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
        if a <= pow(10,6) and n <= pow(10,4) and m <= pow(10,6):
            print(fast_modular_exponentiation(a, n, m))
        else:
            print("Invalid input !")
    else:
        print("Invalid option !")
main()
