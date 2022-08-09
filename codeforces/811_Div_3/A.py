t = int(input())

for i in range(t):
    n,h,m = list(map(int, input().split()))
    h_arr = []
    m_arr = []
    for j in range(n):
        t1, t2 = list(map(int, input().split()))
        h_arr.append(t1)
        m_arr.append(t2)
    minim = 1440
    for j in range(n):
        d1 = h_arr[j]-h
        d2 = m_arr[j]-m
        if(d1 < 0):
            d1+=24
        if(d2 < 0):
            if d1 > 0:
                d1-=1
                d2+=60
            else:
                d1 = 23
                d2+=60
        if(minim > d1*60+d2):
            minim = d1*60+d2
    print(minim//60, minim%60)