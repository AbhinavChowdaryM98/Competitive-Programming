t = int(input())

for i in range(t):
    n = int(input())
    arr = [[], []]
    a = list(input())
    tmp = list(input())
    arr[0] = list(a.copy())
    arr[1] = list(tmp.copy())
    flag = True
    for i in range(2):
        for j in range(n-1):
            if(arr[i][j] != "1"):
                if(i == 0):
                    if(arr[i][j+1] == "1" and arr[i+1][j+1] == "1"):
                        flag = False
                        break
                else:
                    if(arr[i][j+1] == "1" and arr[i-1][j+1] == "1"):
                        flag = False
                        break
    if(flag == True):
        print("YES")
    else:
        print("NO")