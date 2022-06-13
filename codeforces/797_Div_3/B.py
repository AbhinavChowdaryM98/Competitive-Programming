t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i]-b[i] for i in range(n)]
    m = max(c)
    flag = True
    for i in range(n):
        if(c[i] != m and b[i] != 0):
            flag = False
            break
        if(c[i] < 0):
            flag = False
            break
    if(flag):
        print("Yes")
    else:
        print("No")