t = int(input())

for i in range(t):
    n = int(input())
    s = input().split(" ")
    for j in range(n):
        s[j] = int(s[j])
    avg = float(sum(s)*2/n)
    for k in range(n-1):
        tmp1 = [s[x] for x in range(0,k+1)]
        tmp2 = [s[x] for x in range(k+1,n)]
        avg1 = float(sum(tmp1)/(k+1))
        avg2 = float(sum(tmp2)/(n-(k+1)))
        #print(k, avg1, avg2)
        if(avg < (avg1+avg2)):
            avg = avg1+avg2
    print(avg)