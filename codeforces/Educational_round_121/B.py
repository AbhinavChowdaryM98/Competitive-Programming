t = int(input())

for i in range(t):
    s = list(map(lambda x: int(x), list(input())))
    flag = False
    ans = ""
    for j in range(len(s)-1):
        if(flag == False and s[j]+s[j+1]>=10):
            ans+=str(s[j]+s[j+1])
            flag = True
        else:
            ans+=str(s[j])
    if(flag == False):
        ans = ans[:-1]
        ans += str(s[-1]+s[-2])
    print(int(ans))