t = int(input())

for i in range(t):
    n = int(input())
    s = input().split(" ")
    if(n > len(s)*2):
        tmp = ""
        left = n - len(s)*2
        for j in s:
            tmp+=j
            if(j[0]==j[1]):
                for k in range(left):
                    tmp+=j[0]
                left=0
        print(tmp)
    elif(n < len(s)*2):
        left = len(s)*2 - n
        tmp = list(set(s))
        ans = ""
        for j in tmp:
            ans+=j
        while(len(ans) < n-1):
            ans += tmp[-1]
        if(len(ans) < n):
            ans += tmp[-1][0]
        print(ans)
    else:
        tmp = ""
        for j in s:
            tmp+=j
        print(tmp)