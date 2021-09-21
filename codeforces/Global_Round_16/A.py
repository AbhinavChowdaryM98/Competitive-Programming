t = int(input().strip())

for z in range(t):
    tmp = input().split(" ")
    n = int(tmp[0])
    s = int(tmp[1])
    mid = int((n+1)/2)
    #arr = [0 for i in range(n)]
    ans = int(s/(n-mid+1))
    print(ans)