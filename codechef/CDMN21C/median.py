t = int(input().strip())

for i in range(t):
    arr = input().split(" ")
    n = int(arr[0])
    k = int(arr[1])
    num = input().split(" ")
    for i in range(len(num)):
        num[i] = int(num[i])
    tmp_arr = num.copy()
    num.sort()
    final_arr = num[-k:]
    #print(final_arr)
    #print(tmp_arr)
    print(final_arr[int((len(final_arr)-1) / 2)])
    for i in tmp_arr:
        if i in final_arr:
            print(i,end=" ")
    print()