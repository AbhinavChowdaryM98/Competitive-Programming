t = int(input())

for i in range(t):
    n = int(input())
    tmp = input().split(" ")
    arr = [int(j) for j in tmp]
    vis = [0 for j in range(max(arr))]
    a = []
    for j in range(n):
        if(vis[arr[j]-1]==0):
            a.append(arr[j]-1)
            vis[arr[j]-1] = 1
        else:
            k = 1
            while(arr[j]>k):
                if(vis[arr[j]-k]==0):
                    break
                else:
                    k+=1
            if(vis[arr[j]-k]==0):
                a.append(arr[j]-k)
                vis[arr[j]-k] = 1
            else:
                a.append(arr[j]-k)
    print(*a)