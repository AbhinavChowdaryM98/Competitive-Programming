t = int(input().strip())

for i in range(t):
    tmp = input().split(" ")
    l = int(tmp[0])
    r = int(tmp[1])
    n = 2*r - (2*l) + 1
    print(n)