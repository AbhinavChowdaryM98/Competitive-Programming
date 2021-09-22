t = int(input())

for i in range(t):
    n = int(input())
    if(n%3==0):
        for i in range(n-2):
            print(3,end="")
        print(63)
    else:
        for i in range(n):
            print(3,end="")
        print()