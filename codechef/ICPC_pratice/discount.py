t = int(input())

for i in range(t):
    n = int(input())
    tmp = []
    cpy = n
    while(cpy>0):
        tmp.append(cpy%10)
        cpy = int(cpy/10)
    tmp.reverse()
    print(tmp)
    if(n<10):
        print(n)
    elif(tmp[1]==0):
        for j in range(2, len(tmp)):
            print(tmp[j], end="")
        print()
    else:
        ind = tmp.index(max(tmp))
        for j in range(len(tmp)):
            if(j!=ind):
                print(tmp[j], end="")
        print()