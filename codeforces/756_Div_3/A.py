t = int(input())

for i in range(t):
    num = list(map(lambda x: int(x), input().strip()))
    ans = 0
    if(num[-1]%2==0):
        print(0)
    else:
        j = 0
        while(num[j]%2!=0):
            j+=1
            if(j==len(num)):
                break
        if(j==0):
            print(1)
        elif(j<len(num)):
            print(2)
        else:
            print(-1)