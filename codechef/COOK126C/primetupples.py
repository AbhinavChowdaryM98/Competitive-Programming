import math

primes = [0 for i in range(1000006)]
for i in range(2,int(math.sqrt(1000006))):
    if(primes[i]==0):
        for j in range(i,int(1000006/i)):
            primes[i*j] = 1
perfect_tupples = []
for i in range(3,1000004):
    if primes[i] == 0 and primes[i+2] == 0:
        perfect_tupples.append((i,i+2))

t = int(input().strip())

for i in range(t):
    n = int(input())
    ans = 0
    for j in perfect_tupples:
        if(j[1]<=n):
            #print(j[0],j[1])
            ans+=1
        else:
            break
    print(ans)