t = int(input())
for i in range(t):
    rules = list(input())
    s = input()
    ans = 0
    prev = rules.index(s[0])
    if(len(s)==1):
        print(ans)
    else:
        for j in range(1,len(s)):
            ans += abs(rules.index(s[j])-prev)
            prev = rules.index(s[j])
        print(ans)