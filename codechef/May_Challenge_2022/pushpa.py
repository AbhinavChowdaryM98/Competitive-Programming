t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # if n > 1:
    #     a.sort()
    #     if(a[-1] == a[-2]):
    #         print(a[-1]+1)
    #     else:
    #         print(a[-1])
    # else:
    #     print(a[0])
    d = dict()
    s = set(a)
    for i in s:
        d[i] = a.count(i) + i - 1
    ans = max(list(d.values()))
    print(ans)