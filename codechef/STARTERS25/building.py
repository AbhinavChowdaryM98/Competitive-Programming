t = int(input())

for i in range(t):
    x, m = input().split(" ")
    x = int(x)
    m = int(m)
    tmp = 1
    n = 0
    while(x > tmp):
        tmp = tmp<<1
        n+=1
    print(max(m-n, 0))
