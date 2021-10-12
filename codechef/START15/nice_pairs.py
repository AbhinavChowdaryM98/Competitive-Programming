t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    for j in range(n):
        s[j] = int(s[j])
    ans = 0
    for j in range(n):
        for k in range(j+1,n):
            if(k-j == abs(s[k]-s[j])):
                ans+=1
    print(ans)