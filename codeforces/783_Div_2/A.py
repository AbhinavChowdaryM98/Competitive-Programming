t = int(input())

for i in range(t):
    n,m = list(map(lambda x: int(x), input().split()))
    s = min(n,m)
    ans = (s-1)*2
    if(n==m):
        print(ans)
    else:
        if(s==1 and abs(n-m) > 1):
            print(-1)
        else:
            u = max(n,m)
            d = u - s
            if(d%2 == 1):
                ans += 2*d - 1
            else:
                ans += 2*d
            print(ans)