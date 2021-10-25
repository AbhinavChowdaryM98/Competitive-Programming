t = int(input())

for i in range(t):
    n, l, x = list(map(lambda x: int(x), input().split(" ")))
    if(x==0):
        print(0)
    else:
        tmp = min(l, n-l)
        print(tmp*x)