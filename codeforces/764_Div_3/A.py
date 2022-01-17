t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(lambda x: int(x), input().split(" ")))
    print(max(a)-min(a))