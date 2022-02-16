t = int(input())
for i in range(t):
    n,m,r,c = list(map(lambda x: int(x), input().split(" ")))
    s = []
    C = 0
    b = [0 for i in range(n)]
    B = 0
    for j in range(n):
        tmp = list(input())
        b[j] += tmp.count('B')
        B += b[j]
        if(tmp[c-1]=='B'):
            C = 1
        s.append(tmp)
    if(B == 0):
        print(-1)
    else:
        if(s[r-1][c-1] == 'B'):
            print(0)
        elif(b[r-1]>0):
            print(1)
        elif(C==1):
            print(1)
        else:
            print(2)