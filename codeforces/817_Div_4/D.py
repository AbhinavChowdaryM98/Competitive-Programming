t = int(input())

def cal_score(a):
    ans = 0
    for itr in range(len(a)):
        if(a[itr] == 'L'):
            ans+=itr
        else:
            ans+=len(a)-1-itr
    return ans

for i in range(t):
    n = int(input())
    s = input()
    val = []
    fh = []
    sh = []
    for j in range(n//2):
        if(s[j] == 'L'):
            fh.append(j)
        if(s[n-1-j] == 'R'):
            sh.append(j)
    # val.append(cal_score(s))
    prev_score = cal_score(s)
    for j in range(n):
        if(len(fh) != 0 and len(sh) != 0):
            if(fh[0]<=sh[0]):
                val.append(prev_score-fh[0]+len(s)-1-fh[0])
                del fh[0]
                prev_score = val[-1]
            else:
                val.append(prev_score-sh[0]+len(s)-1-sh[0])
                del sh[0]
                prev_score = val[-1]
        elif (len(fh) != 0 or len(sh) != 0):
            if(len(fh) > 0):
                while(len(fh)):
                    val.append(prev_score-fh[0]+len(s)-1-fh[0])
                    del fh[0]
                    prev_score = val[-1]
                break
            else:
                while(len(sh)):
                    val.append(prev_score-sh[0]+len(s)-1-sh[0])
                    del sh[0]
                    prev_score = val[-1]
                break
    # tmp = val[-1]
    while(len(val) < n):
        val.append(prev_score)
    print(*val)


