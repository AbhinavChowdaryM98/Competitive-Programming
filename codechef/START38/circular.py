t = int(input())

for i in range(t):
    a,b,m = list(map(int, input().split()))
    print(min(abs(a-b), (m - abs(a-b))))