t = int(input())

for i in range(t):
    tmp = input()
    ans = 0
    path = ["" for i in range(8)]
    s = [0 for i in range(8)]
    for j in range(8):
        path[j] += str(input())
        s[j] = list(path[j]).count("#")
    for j in range(1,7):
        if(s[j] == 1 and (s[j-1]==2 and s[j+1]==2)):
            ans = j
            break
    print(ans+1,path[ans].index("#")+1)