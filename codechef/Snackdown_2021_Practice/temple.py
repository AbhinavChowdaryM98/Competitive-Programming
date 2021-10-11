t = int(input())

for i in range(t):
    n = int(input())
    arr = input().split(" ")
    for j in range(n):
        arr[j] = int(arr[j])
    if(n%2==0 or arr[0]!=1):
        print("no")
    else:
        req = [j+1 for j in range(int((n+1)/2))]
        for k in range(int((n+1)/2), n):
            req.append(req[k-1]-1)
        flag = True
        #print(*req)
        #print(*arr)
        for l in range(n):
            if(arr[l]!=req[l]):
                flag = False
                break
        if(flag):
            print("yes")
        else:
            print("no")