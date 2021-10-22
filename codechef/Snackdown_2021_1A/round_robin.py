t = int(input())

for i in range(t):
    n,k = map(lambda x: int(x),input().split(" "))
    matches = int(n*(n-1)/2)
    if(n%2 == 0):
        if(n==k):
            print(int(n/2)-1)
    else:
        if(n==k):
            print(int((n)/2))