t = int(input())

for i in range(t):
    c = int(input())
    binary = []
    cpy = c
    while(cpy>0):
        if(cpy%2==0):
            binary.insert(0,0)
        else:
            binary.insert(0,1)
        cpy = int(cpy/2)
    pres = 1
    arr = [len(binary)]
    for j in range(1,len(binary)):
        if(binary[j]==pres):
            continue
        else:
            arr.append(len(binary)-j)
            pres = (pres+1)%2
    for j in range(len(arr)):
        arr[j] = 1<<arr[j]
        arr[j]-=1
    arr.sort()
    print(*arr)