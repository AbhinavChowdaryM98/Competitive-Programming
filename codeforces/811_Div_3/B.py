t = int(input())

for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    ans = 0
    vis = [0 for j in range(n+1)]
    for j in range(1,n+1):
        if(vis[ar[n-j]]==1):
            break
        else:
            vis[ar[n-j]] = 1
            ans+=1
    print(n-ans)