import io, os, sys
input = io.BytesIO(os.read(0, \
         os.fstat(0).st_size)).readline

t = input().decode()
t = int(t)

for i in range(t):
    tmp = input().decode().split(" ")
    n = int(tmp[0])
    m = int(tmp[1])
    x = int(tmp[2])
    y = int(tmp[3])
    ans = 0
    tmp2 = min(n,m)
    pres_n = tmp2
    pres_m = tmp2
    ans += min(y*(tmp2-1), 2*x*(tmp2 - 1))
    tmp3 = max(n,m)
    check = True
    if(n>m):
        check=False
    if(y<x):
        if(check):
            ans = ans + 2*y*(int((tmp3-pres_m)/2))
            if((tmp3 - pres_m)%2 != 0):
                ans += x
        else:
            ans+=2*y*(int((tmp3-pres_n)/2))
            if((tmp3 - pres_n)%2 > 0):
                ans += x
    else:
        ans += x*(tmp3 - pres_n)
    sys.stdout.write(str(ans)+"\n")