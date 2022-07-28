t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d_freq = {}
    maxval = -1
    maxcnt = 0
    for i in arr:
        try:
            d_freq[i] += 1
            if(d_freq[i] > maxval):
                maxval = d_freq[i]
                maxcnt = 1
            elif (d_freq[i] == maxval):
                maxcnt+=1
        except:
            d_freq[i] = 1
            if(d_freq[i] > maxval):
                maxval = d_freq[i]
                maxcnt = 1
            elif (d_freq[i] == maxval):
                maxcnt+=1
    if(maxcnt > 1):
        print(maxval)
    else:
        tmp = (maxval+1)//2
        maxar = []
        for i in d_freq.keys():
            if(d_freq[i] < maxval):
                maxar.append(d_freq[i])
        try:
            tmp2 = max(maxar)
            print(max(tmp, tmp2))
        except:
            print(tmp)