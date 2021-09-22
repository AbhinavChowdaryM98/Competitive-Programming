def per_value(i):
    return i[0]/i[1]

t = int(input())

for i in range(t):
    ar = input().split(" ")
    a = int(ar[0])
    b = int(ar[1])
    c = int(ar[2])
    xy = input().split(" ")
    x = int(xy[0])
    y = int(xy[1])
    z = int(xy[2])
    arr = [[x,a,20], [y,b,20], [z,c,20]]
    arr.sort(key=per_value)
    #print(*arr)
    while (arr[0][2]*a+arr[1][2]*b+arr[2][2]*c > (240 + a) and arr[0][2]>0):
        arr[0][2]-=1
    if(arr[0][2]==0):
        while(arr[1][2]*b+arr[2][2]*c > (240 + b) and arr[1][2]>0):
            arr[1][2]-=1