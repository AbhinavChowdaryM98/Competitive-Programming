t = int(input())

for i in range(t):
    n = int(input())
    d = {}
    per = []
    for j in range(3):
        s = list(input().split(" "))
        per.append(s)
    for a in per:
        for b in a:
            try:
                if(d[b] == 3):
                    d[b] = 1
                else:
                    d[b] = 0
            except:
                d[b]=3
    ans = [0 for i in range(3)]
    for j in range(3):
        for ele in per[j]:
            ans[j]+=d[ele]
    print(*ans)