t = int(input())

for i in range(t):
    n = int(input())
    ar = []
    max = 9
    while(n >= max):
        n-=max
        ar.append(max)
        max-=1
        if(n == 0):
            break
    if(n > 0):
        ar.append(n)
    ans = 0
    for j in range(1, len(ar)+1):
        ans *= 10
        ans += ar[len(ar)-j]
    print(ans)