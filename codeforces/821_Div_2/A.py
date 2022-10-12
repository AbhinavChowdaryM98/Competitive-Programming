t = int(input())
 
for i in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if(n == k):
        print(sum(a))
    else:
        tmax = [-1 for x in range(k)]
        for j in range(k):
            tmp = j
            while(tmp < n):
                if(tmax[j] < a[tmp]):
                    tmax[j] = a[tmp]
                tmp+=k
        print(sum(tmax))