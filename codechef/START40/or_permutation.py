def get_and(l):
    t = l[0]
    for i in range(1,len(l)):
        t = t & l[i]
    return t

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = get_and(b)
    cp_a = []
    for i in range(n):
        cp_a.append(a[i] | x)
    s_a = set(cp_a)
    dict_a = {}
    for i in s_a:
        dict_a[i] = 0
    for i in cp_a:
        dict_a[i]+=1
    flag = True
    for i in b:
        try:
            dict_a[i]-=1
        except:
            flag = False
            break
    if flag:
        for i in dict_a.keys():
            if dict_a[i] != 0:
                flag = False
                break
    if flag == True:
        print(x)
    else:
        print(-1)