t = int(input())

for i in range(t):
    n = int(input())
    a = 3; b = 2; c = 1
    n-=6
    a+=(n//3)
    b+=(n//3)
    c+=(n//3)
    left = n%3
    a+= left
    while(a-3 > b):
        a-=2
        b+=1
        c+=1
    while(a-2 > b):
        a-=1
        b+=1
    print(b, " ", a, " ", c)