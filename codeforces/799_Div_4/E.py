t = int(input())

for i in range(t):
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    actual = sum(a)
    if(s>actual):
        print(-1)
    elif (s == actual):
        print(0)
    else:
        tmp = a.copy()
        while(actual>s):
            f = 0;e = len(tmp)-1
            while(a[f]==0):
                f+=1
            while(a[e]==0):
                e-=1
            if (f < len(tmp)-e):
                