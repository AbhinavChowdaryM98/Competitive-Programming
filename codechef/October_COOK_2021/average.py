t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(lambda x: int(x), input().split(" ")))
    arr.sort()
    less = [0 for j in range(n)]
    great = [0 for j in range(n)]
    less[n-1] = n
    for j in range(2,n+1):
        if(arr[n-j] == arr[n-j+1]):
            less[n-j] = less[n-j+1]
            great[n-j] = great[n-j+1]
        else:
            less[n-j] = n-j+1
            great[n-j] = j - 1
    #print(arr)
    #print(less)
    #print(great)
    for j in range(n):
        if(less[j]>great[j]):
            print(n-j)
            break