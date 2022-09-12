ch = list('abcdefghijklmnopqrstuvwxyz')
t = int(input())
d = {}

for j in range(26):
    d[ch[j]] = j+1

def myfunc(a):
    return d[a[0]]

for i in range(t):
    s = input()
    cost = abs(d[s[-1]]-d[s[0]])
    l = []
    if(d[s[0]] > d[s[-1]]):
        for j in range(1,len(s)):
            if(d[s[j]] <= d[s[0]] and d[s[j]] >= d[s[-1]]):
                l.append((s[j], j+1))
        l.sort(key=myfunc)
        ar = [1]
        for j in range(len(l)):
            ar.append(l[len(l)-1-j][1])
        print(cost, len(l)+1)
        print(*ar)
    elif (d[s[-1]] > d[s[0]]):
        for j in range(1,len(s)):
            if(d[s[j]] >= d[s[0]] and d[s[j]] <= d[s[-1]]):
                l.append((s[j], j+1))
        l.sort(key=myfunc)
        ar = [1]
        for ele in l:
            ar.append(ele[1])
        print(cost, len(l)+1)
        print(*ar)
    else:
        ar = [1]
        j = 1
        while(j < len(s)):
            if(s[j] == s[0]):
                ar.append(j+1)
            j+=1
        print(0, len(ar))
        print(*ar)