t = int(input())

for i in range(t):
    n = int(input())
    for j in range(n):
        if(j%2==0):
            print(j+1, end=" ")
        else:
            print(j-1, end=" ")
    print()