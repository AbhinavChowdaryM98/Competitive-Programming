ch = list('abcdefghijklmnopqrstuvwxyz')
t = int(input())
d = {}

for j in range(26):
    d[ch[j]] = j+1

def get_min(sr, c, vis):
    tmax = 27
    max_ind = -1
    for i in range(len(sr)):
        if(vis[i] == 0):
            if(d[sr[i]] >= d[c]):
                if(tmax > d[sr[i]]):
                    tmax = d[sr[i]]
                    max_ind = i
    return max_ind


def get_max(sr, c, vis):
    tmax = -1
    max_ind = -1
    for i in range(len(sr)):
        if(vis[i] == 0):
            if(d[sr[i]] <= d[c]):
                if(tmax < d[sr[i]]):
                    tmax = d[sr[i]]
                    max_ind = i
    return max_ind

for i in range(t):
    # n = int(input())
    m = 1
    s = input()
    ar = [1]
    vis = [0 for i in range(len(s))]
    prev = 1
    vis[0] = 1
    if(d[s[0]] > d[s[-1]]):
        while(prev != len(s)):
            nxt = get_max(s, s[prev-1], vis)
            vis[nxt]=1
            ar.append(nxt+1)
            prev = nxt+1
        print(abs(d[s[0]]-d[s[-1]]), len(ar))
        print(*ar)
    elif(d[s[0]] < d[s[-1]]):
        while(prev != len(s)):
            nxt = get_min(s, s[prev-1], vis)
            vis[nxt]=1
            ar.append(nxt+1)
            prev = nxt+1
        print(abs(d[s[0]]-d[s[-1]]), len(ar))
        print(*ar)
    else:
        j = 1
        while(j < len(s)):
            if(s[j] == s[0]):
                ar.append(j+1)
            j+=1
        print(0, len(ar))
        print(*ar)