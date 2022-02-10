t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(lambda x: int(x), input().split(" ")))
    flag = True
    tmp_dict = {i:0 for i in range(n+1)}
    for j in range(len(arr)):
        tmp_dict[arr[j]]+=1
    for j in range(n):
        if(tmp_dict[j]>1):
            pass
        elif((tmp_dict[j] == 1)):
            flag = False
            break
        else:
            flag = True
            break
    if(flag):
        print("YES")
    else:
        print("NO")
