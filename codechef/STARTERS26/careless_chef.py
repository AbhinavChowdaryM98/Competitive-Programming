t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(lambda x: int(x), input().split(" ")))
    sum = 0
    for j in arr:
        sum+=j
    if(sum%2 == 0):
        print("YES")
    else:
        print("NO")