ch = list('abcdefghijklmnopqrstuvwxyz')
t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    a = []
    k = 0
    while(k <n):
        if(s[n-1-k] == '0'):
            tmp = n-1-k
            a.insert(0, int(s[tmp-2]+s[tmp-1]))
            k+=3
        else:
            a.insert(0, int(s[n-1-k]))
            k+=1
    ans = ''
    for j in range(len(a)):
        ans+=ch[a[j]-1]
    print(ans)