t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    r = input()
    ans = 0
    for j in range(n):
        if(s[j] != r[j]):
            ans+=1
    if(ans%2 == 0):
        print(1)
    else:
        print(0)