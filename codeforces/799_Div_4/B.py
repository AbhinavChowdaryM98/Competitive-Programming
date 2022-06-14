t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    t = set(a)
    if((n-len(t))%2 == 1):
        print(len(t)-1)
    else:
        print(len(t))