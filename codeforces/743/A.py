t = int(input())

for i in range(t):
    n = int(input())
    l = input()
    ans = 0
    if(int(l[-1])>0):
        ans+=int(l[-1])
    for i in range(n - 1):
        if(int(l[i])>0):
            ans+=int(l[i])
            ans+=1
    print(ans)