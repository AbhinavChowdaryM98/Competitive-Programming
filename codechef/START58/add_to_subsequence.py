# cook your dish here
def max_freq(arr):
    d = {}
    tmax = 1
    for i in range(len(arr)):
        try:
            d[arr[i]] += 1
            if(tmax < d[arr[i]]):
                tmax = d[arr[i]]
        except:
            d[arr[i]] = 1
    return tmax

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # tmax =  max_freq(arr)
    d = {}
    vis = []
    j = 0
    while (j < n):
        try:
            d[arr[j]]+=1
            vis.append(j)
            d.clear()
            j-=1
        except:
            d[arr[j]] = 1
        j+=1
    # print(max(len(vis), tmax-1))
    print(len(vis))
    print(*vis)