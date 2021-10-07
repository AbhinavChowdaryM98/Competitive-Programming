t = int(input())

for i in range(t):
    n = int(input())
    tmp = input().split(" ")
    even = 0
    ans = 0
    for j in tmp:
        if(int(j)%2 == 0):
            even+=1
    if(even <= int((n+1)/2)):
        ans += even
        ans += (n - int((n+1)/2))
    else:
        ans += (n - even)
        ans += int((n+1)/2)
    print(ans)