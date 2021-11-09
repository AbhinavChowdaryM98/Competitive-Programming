t = int(input())
name = ["RAMADHIR", "SAHID"]
for i in range(t):
    size = int(input())
    s = input()
    tmp = s[0]
    ans = 0
    blocks = []
    j = 0
    while(j<size):
        p = []
        while(j<size and tmp==s[j]):
            p.append(s[j])
            j+=1
        if(j<size):
            tmp = s[j]
        blocks.append(p)
    n = len(blocks)
    while(n>0):
        if(n%2==1):
            n-=1
            ans = (ans+1)%2
        else:
            if(len(blocks)>2):
                n-=2
            else:
                n-=1
            ans = (ans+1)%2
    print(name[ans])