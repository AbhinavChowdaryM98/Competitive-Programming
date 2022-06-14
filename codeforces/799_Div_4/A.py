t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    ans = 0
    for j in range(1,4):
        if(a[j]>a[0]):
            ans+=1
    print(ans)