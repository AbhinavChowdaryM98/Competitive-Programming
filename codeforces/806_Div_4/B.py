t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    tmp = set(list(s))
    print(n+len(tmp))