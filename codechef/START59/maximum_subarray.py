# cook your dish here
def max_sub_sum(arr):
    tmp_max = max(arr)
    tmp = 0
    for i in range(len(arr)):
        tmp += arr[i]
        if(tmp > tmp_max):
            tmp_max = tmp
        if(tmp < 0):
            tmp = 0
    return tmp_max

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    max_sub = max_sub_sum(arr)
    amax = -100000008
    # aind = [-1,-1]
    tmp = 0
    for j in range(n):
        tmp+=arr[j]
        if(amax < tmp):
            amax = tmp
            # aind[0] = 0
            # aind[1] = j
    tmp = 0
    for j in range(n):
        tmp+=arr[n-1-j]
        if(amax < tmp):
            amax = tmp
            # aind[0] = j
            # aind[1] = n-1
    for j in range(m):
        if(b[j] > 0):
            amax+=b[j]
    print(max(max_sub, amax))