t = int(input())

for i in range(t):
    tmp = input().split(" ")
    n = int(tmp[0])
    k = int(tmp[1])
    if(n-k == 1):
        print(-1)
    else:
        for j in range(k):
            print(j+1,end=" ")
        if(k!=n):
            for l in range(k+1, n):
                print(l+1, end=" ")
            print(k+1)
        else:
            print()