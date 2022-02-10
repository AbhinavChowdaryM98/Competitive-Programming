t = int(input())

for i in range(t):
    n = int(input())
    x = []
    y = []
    for j in range(n):
        tmpx, tmpy = input().split(" ")
        x.append(int(tmpx))
        y.append(int(tmpy))
    unique_x = set(x)
    unique_y = set(y)
    print(len(unique_x)+len(unique_y))
