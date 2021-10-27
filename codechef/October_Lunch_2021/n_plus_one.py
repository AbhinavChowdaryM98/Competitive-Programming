t = int(input())

for i in range(t):
    n = int(input())
    j = 1
    lim = i<<(n-1)
    print(1, end=" ")
    for k in range(n):
        print(j, end=" ")
        j*=2
    print()