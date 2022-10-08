# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ev = 0
    odd = 0
    for j in range(n):
        if(arr[j]%2 == 0):
            ev += 1
        else:
            odd += 1
    if(odd > 0):
        print(ev)
    else:
        print(0)