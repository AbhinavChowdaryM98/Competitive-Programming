t = int(input())

for i in range(t):
    n,m = list(map(int, input().split()))
    r2 = n//2
    c2 = m//2
    # a2 = r2*c2*4
    # fa = n*m - a2
    print(n*m - r2*c2*4)