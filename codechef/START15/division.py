t = int(input())

for i in range(t):
    n,a,b = input().split(" ")
    n,a,b = int(n),int(a),int(b)
    total = 0
    if(a<b):
        tmp = 0
        cpy = n
        while(cpy%2==0):
            tmp+=1
            cpy = cpy/2
        if(a>0):
            total += (tmp)*a
            tmp2 = 3
            while(cpy!=1):
                if(cpy%tmp2==0):
                    total+=b
                    cpy = cpy/tmp2
                else:
                    tmp2+=2
        if(a<0 and b>=0):
            if(tmp>0):
                total+=a
            tmp2 = 3
            while(cpy!=1):
                if(cpy%tmp2==0):
                    total+=b
                    cpy = cpy/tmp2
                else:
                    tmp2+=2
        if(b<0):
            if(tmp):
                total = a
            else:
                total = b
    else:
        tmp = 0
        cpy = n
        while(cpy%2==0):
            tmp+=1
            cpy = cpy/2
        if(b>0):
            total += (tmp)*a
            tmp2 = 3
            while(cpy!=1):
                if(cpy%tmp2==0):
                    total+=b
                    cpy = cpy/tmp2
                else:
                    tmp2+=2
        if(b<0 and a>=0):
            if(tmp>0):
                total += tmp*a
            else:
                total += b
        if(a<0):
            if(tmp>0):
                total = a
            else:
                total = b
    print(total)