t = int(input())

for i in range(t):
    a,b,c = list(map(int, input().split()))
    l1 = a-1
    l2 = 0
    if(b < c):
        l2 = c-b + c-1
    else:
        l2 = b-1
    if(l1 < l2):
        print(1)
    elif(l2 < l1):
        print(2)
    else:
        print(3)