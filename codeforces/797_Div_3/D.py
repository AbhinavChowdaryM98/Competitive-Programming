t = int(input())

for i in range(t):
    n,k = list(map(int, input().split()))
    s = list(input())
    len = s[0:k].count("B")
    tmp = len
    for i in range(1,n-k+1):
        if(s[i-1]!=s[i+k-1]):
            if(s[i+k-1] == "B"):
                tmp+=1
            else:
                tmp-=1
        if(tmp > len):
            len = tmp
        if(len == k):
            break
    print(k-len)