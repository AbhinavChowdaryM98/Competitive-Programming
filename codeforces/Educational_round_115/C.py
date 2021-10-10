t = int(input())

for i in range(t):
    n = int(input())
    arr = input().split(" ")
    sum = 0
    vis = [0 for i in range(n)]
    for i in range(n):
        arr[i] = int(arr[i])
        sum += arr[i]
    avg = sum/n
    ans = 0
    for i in range(n-1):
        tmp = arr[i+1:]
        if (2*avg - arr[i]) in tmp:
            ans += tmp.count((2*avg - arr[i]))
    print(ans)