t = int(input())
for i in range(t):
    s = input()
    tmp = set(list(s))
    dict = {j:0 for j in tmp}
    for j in range(len(s)):
        dict[s[j]]+=1
    ans = ""
    for j in dict.keys():
        ans+= (j*dict[j])
    print(ans)