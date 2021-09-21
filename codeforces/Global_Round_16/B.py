t = int(input().strip())

def mex(duck):
    arr = [[1,duck[0]]]
    prev = duck[0]
    for i in duck:
        if(prev==i):
            arr[-1][0]+=1
        else:
            arr.append([1,i])
            prev = i
    return arr

def mex_value(s):
    if(s == '0'):
        return 1
    return 0

for z in range(t):
    s = input()
    cnt_0 = s.count('0')
    cnt_1 = s.count('1')
    cnt_2 = s.count('2')
    if(cnt_0 == 0):
        ans = 0
        print(ans)
    else:
        arr = mex(s)
        ans_mex = 0
        for i in arr:
            ans_mex += i[0]*mex_value(i[1])
        ans_gen = 0
        if(cnt_1==0):
            ans_gen = 1
        elif(cnt_2==0):
            ans_gen = 2
        ans = min(ans_gen, ans_mex)
        print(ans, ans_gen, ans_mex)