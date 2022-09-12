def check_merge(a):
    ans = [a[k] for k in range(len(a))]
    i = 0
    while (i < len(ans)-1):
        if(ans[i][1] >= ans[i+1][0]):
            if(ans[i][1] > ans[i+1][1]):
                # del ans[i+1]
                ans.pop(i+1)
            else:
                ans[i][1] = ans[i+1][1]
                # del ans[i+1]
                ans.pop(i+1)
        else:
            i+=1
    return ans

def tinsert(intervals, new_interval):
    if(new_interval[0] > new_interval[1]):
        sw = new_interval[0]
        new_interval[0] = new_interval[1]
        new_interval[1] = sw
    for i in xrange(len(intervals)):
        if(intervals[i][0] > new_interval[0]):
            intervals.insert(i, new_interval)
            break
        elif(intervals[i][0] == new_interval[0]):
            intervals[i][1] = max(new_interval[1], intervals[i][1])
            break
    if(new_interval[0] > intervals[-1][0]):
        intervals.append(new_interval)
        return intervals
    return check_merge(intervals)

a = [[1,2], [3,6]]
b = [10, 8]

ans = tinsert(a,b)

print(ans)
