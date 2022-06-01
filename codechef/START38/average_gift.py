t = int(input())

for i in range(t):
    n, x = list(map(int, input().split()))
    s = list(map(int, input().split()))
    if(min(s) > x or max(s) < x):
        print("No")
    else:
        print("Yes")