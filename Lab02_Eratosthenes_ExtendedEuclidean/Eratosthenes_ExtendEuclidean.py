import math

def sieve_of_eratosthenes(n: int)->list[int]:
    if (n < 2):
        return []
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, math.isqrt(n)+1):
        if (is_prime[i]):
            for j in range(i*i, n, i):
                is_prime[j] = False
    return [i for i in range(n) if (is_prime[i])]

def euclidean_extend(a,b):
    if (b == 0):
        d = a; x = 1; y = 0
        return d, x, y
    else:
        d, x1, y1 = euclidean_extend(b, a%b)
        q = a//b
        x = y1
        y = x1 - y1*q
        return d, x , y
    
def main():
    print("1: Sieve of Eratosthenes\n2: Euclidean Extend")
    case = int(input("Enter selection: "))
    if (case == 1):
        n = int(input("Enter n: "))
        print(sieve_of_eratosthenes(n))
    elif (case == 2):
        print("The equation has the form: ax + by = d")
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        if (a >= 0 and b >= 0):
            print("(d, x, y) =",euclidean_extend(a,b))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
main()
    
