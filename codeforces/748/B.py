arr = {0:[0,5], 5:[2,7]}
ind = [0,5]

t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    if(n%25 == 0):
        print(ans)
    else:
        while(n%10 not in ind):
            n = int(n/10)
            ans+=1
        tmp = int(n/10)
        tmp2 = n%10
        while(tmp%10 not in arr[tmp2]):
            tmp = int(tmp/10)
            ans+=1
        print(ans)