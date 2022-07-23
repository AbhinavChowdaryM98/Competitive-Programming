t = int(input())

for i in range(t):
    a,b,n = list(map(int, input().split()))
    if(a%b == 0):
        print(-1)
    else:
        tmp = n//a
        if(tmp*a < n):
            tmp+=1
        while(tmp*a % b == 0):
            tmp+=1
        print(tmp*a)
