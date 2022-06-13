t = int(input())

for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [t[0]-s[0]]
    for i in range(1, n):
        ans.append(t[i]-(max(t[i-1], s[i])))
    print(*ans)