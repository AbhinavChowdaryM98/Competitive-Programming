dict = [0]
tmp = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    dict.append(tmp[i])
t = int(input())
for i in range(t):
    s = list(input())
    s.sort()
    ans = 0
    for j in range(len(s)):
        ans += (j+1)*(dict.index(s[j]))
    print(ans)