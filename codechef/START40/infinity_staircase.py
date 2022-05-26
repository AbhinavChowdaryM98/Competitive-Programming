t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        n -= 1
        ans = n//5
        ans = ans*2
        if(n%5 < 4 and n%5 > 0):
            ans+=1
        elif n%5==4:
            ans+=2
        print(ans)