t = int(input())

for i in range(t):
    size = int(input())
    s = input()
    tmp = s[0]
    ans = 1
    for j in range(1,size):
        if(s[j]!=tmp):
            tmp = s[j]
            ans+=1
    if(ans%2==1):
        print("SAHID")
    else:
        print("RAMADHIR")