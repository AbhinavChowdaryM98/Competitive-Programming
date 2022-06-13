t = int(input())

for i in range(t):
    n,k = list(map(int, input().split()))
    a = [i+1 for j in range(k-1)]
    b = 0
    if(k==1):
        b = n%2
    else:
        if(k%2 == 1):
            while(len(a)>1):
                del a[k%len(a)]
            b = a[0]%2
        else:
            b = a[-1]%2
    if(b == 1):
        print("Odd")
    else:
        print("Even")