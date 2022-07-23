t = int(input())

for i in range(t):
    x,y,n,r = list(map(int, input().split()))
    d = y - x
    tmp = r - n*x
    if(tmp < 0):
        print(-1)
    else:
        ans = tmp//d
        print(max(0, n-ans), min(n,ans
