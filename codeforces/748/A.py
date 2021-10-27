t = int(input())
for i in range(t):
    arr = list(map(lambda x: int(x), input().split(" ")))
    tmp = max(arr)
    if(arr.count(tmp)>1):
        for j in range(3):
            arr[j] = tmp - arr[j]
            arr[j]+=1
    else:
        for j in range(3):
            arr[j] = tmp - arr[j]
            if(arr[j] != 0):
                arr[j]+=1
    print(*arr)