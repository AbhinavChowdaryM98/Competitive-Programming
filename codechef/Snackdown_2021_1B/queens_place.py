t = int(input())
for i in range(t):
    n = int(input())
    for j in range(3):
        for k in range(n):
            if(j==1 and k==1):
                print('Q', end="")
            else:
                print('.', end="")
        print()
    for j in range(3,n):
        for k in range(n):
            if(j==k):
                print('Q', end="")
            else:
                print('.', end="")
        print()