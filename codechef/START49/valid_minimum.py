t = int(input())

for i in range(t):
    l = list(map(int, input().split()))
    if(l.count(min(l)) < 2):
        print("No")
    else:
        print("Yes")