t = int(input())

for i in range(t):
    n,k = input().split(" ")
    n,k = int(n),int(k)
    arr = input().split(" ")
    for j in range(n):
        arr[j] = int(arr[j])
    arr.sort(reverse=True)
    tmp = arr[k:].count(arr[k-1])
    print(k+tmp)