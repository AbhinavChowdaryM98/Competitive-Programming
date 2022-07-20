def left_over(ar,cp_n):
    left = []
    j = 0
    while(j < cp_n):
        # print(j)
        if(ar[j] <= j):
            left.append(ar[j])
            del ar[j]
            cp_n -= 1
        else:
            j+=1
    return left

def check(a):
    for i in range(len(a)):
        if(a[i] > i):
            continue
        else:
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    cp_n = n
    ar = list(map(int, input().split()))
    # ans = 1
    if(check(ar)):
        print(1)
    else:
        ans_lists = [ar.copy()]
        # print(ans_lists)
        while(check(ans_lists[-1]) == False):
            ans_lists[-1].sort()
            tmp = left_over(ans_lists[-1], len(ans_lists[-1]))
            ans_lists.append(tmp)
        print(len(ans_lists))
        # print(tmp)