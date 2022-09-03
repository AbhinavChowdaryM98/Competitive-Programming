t = int(input())

for i in range(t):
    # ans = 0
    rects = [[0 for x in range(1003)] for y in range(1003)]
    n,q = list(map(int, input().split(" ")))
    # rect = {}
    for j in range(n):
        a,b = list(map(int, input().split(" ")))
        rects[a][b] += 1
    for j in range(q):
        ans = 0
        hs,ws,hb,wb = list(map(int, input().split(" ")))
        # rows = rects[hs+1:hb]
        # res_rect = [k[ws+1:wb] for k in rows]
        for x in range(hs+1, hb):
            for y in range(ws+1, wb):
                if(rects[x][y] != 0):
                    ans += x*y*rects[x][y]
        print(ans)
