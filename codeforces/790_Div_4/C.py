w = list("abcdefghijklmnopqrstuvwxyz")

w_dict = {}

for i in range(26):
    w_dict[w[i]] = i+1

def dist(s1,s2):
    result = 0
    for i in range(len(s1)):
        result += abs(w_dict[s1[i]]-w_dict[s2[i]])
    return result

t = int(input())

for i in range(t):
    n,s = list(map(int, input().split()))
    strings = []
    for j in range(n):
        tmp = input()
        strings.append(tmp)
    ans = 9*26
    for j in range(n):
        for k in range(j+1,n):
            tmp = (dist(strings[j], strings[k]))
            if(tmp < ans):
                ans = tmp
    print(ans)