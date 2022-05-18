t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    while(i < len(a)-1):
        if(a[i] == a[i+1]):
            del a[i+1]
        else:
            i+=1
    print(len(a))