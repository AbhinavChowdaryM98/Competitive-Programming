t = int(input())

for i in range(t):
    ar = []
    n = int(input())
    for j in range(n):
        tmp = [int(k) for k in list(input())]
        ar.append(tmp)
    # print(ar)
    mid = n//2
    ans = 0
    for j in range(mid):
        u = [ar[j][k] for k in range(j,n-j)]
        r = [ar[k][n-j-1] for k in range(j,n-j)]
        d = [ar[n-j-1][k] for k in range(j,n-j)]
        l = [ar[k][j] for k in range(j,n-j)]
        for k in range(n-2*j-1):
            sum = u[k]+r[k]+d[len(d)-1-k]+l[len(l)-1-k]
            ans+=min(sum, 4-sum)
    print(ans)