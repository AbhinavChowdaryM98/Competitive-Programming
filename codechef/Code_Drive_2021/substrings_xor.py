t = int(input())
for i in range(t):
    n, k = list(map(lambda x: int(x), input().split(" ")))
    s = input()
    prefix_sum = [int(s[0])]
    for j in range(1,len(s)):
        if(s[j]=="1"):
            prefix_sum.append(prefix_sum[j-1]+1)
        else:
            prefix_sum.append(prefix_sum[j-1])
    #print(prefix_sum)
    prefix_sum[0]=0
    ans =""
    print(prefix_sum)
    for i in range(k):
        ans+=str((prefix_sum[i+n-k]-prefix_sum[i])%2)
    print(ans)
    print(ans.count("1"))