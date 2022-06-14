# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if(n%2 == 1):
        print(-1)
    else:
        s = sum(a)
        print(abs(s)//2)