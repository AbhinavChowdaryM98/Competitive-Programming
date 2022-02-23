prr = [0 for i in range(100000)]

for i in range(2, 100000):
    if(prr[i] == 0):
        for j in range(int(100000/i)):
            prr[i*j] = 1
primes = [i for i in range(100000) if prr[i] == 0]

def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

def find_scf(a,b):
    if(a%2 == 0):
        return 1, 2
    elif(b%2 == 0):
        return 0, 2
    else:
        for i in range(len(primes)):
            if(a%primes[i] == 0):
                return 1, primes[i]
            elif(b%primes[i] == 0):
                return 0, primes[i]

t = int(input())

for i in range(t):
    n = int(input())
    max = int((2*n)/3)
    arr = list(map(lambda x: int(x), input().split()))
    done = 0
    for i in range(n-1):
        if(computeGCD(arr[i],arr[i+1])==1):
            f, mul = find_scf(arr[i],arr[i+1])
            arr[i+f] = arr[i+f]*mul
            done += 1
            if(done > max):
                break
    print(*arr)