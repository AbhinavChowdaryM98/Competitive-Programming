# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tmax = max(arr)
    if(arr[0] == tmax):
        print(-1)
    else:
        j = 1
        while(arr[j] != tmax):
            j+=1
        arr1 = arr[:j]
        arr2 = arr[j:]
        print(j)
        print(*arr1)
        print(n-j)
        print(*arr2)