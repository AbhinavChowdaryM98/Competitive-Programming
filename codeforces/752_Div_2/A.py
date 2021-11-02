t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(lambda x: int(x), input().split(" ")))
    ind = a.index(max(a))
    print(max(a)-1-ind)