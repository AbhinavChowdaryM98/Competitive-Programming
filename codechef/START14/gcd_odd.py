t = int(input())

for i in range(t):
    n = int(input())
    arr = input().split(" ")
    for j in range(n):
        arr[j] = int(arr[j])
    ans = 0
    while(1):
        tmp = True
        for j in range(n):
            if arr[j]%2 != 0:
                tmp = False
                break
            arr[j] = int(arr[j]/2)
        if tmp == False:
            print(ans)
            break
        ans+=1