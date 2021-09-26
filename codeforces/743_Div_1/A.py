t = int(input())
ans = []
for i in range(t):
    n = int(input())
    read_and_understand = [0 for x in range(n+1)]
    understand = [[] for x in range(n+1)]
    for j in range(1,n+1):
        l = input().split(" ")
        for z in range(1,len(l)):
            understand[j].append(int(l[z]))
    num = 0
    prev = []
    while(1):
        for m in range(1,n+1):
            if(len(understand[m])==0):
                read_and_understand[m]=1
            else:
                tmp = True
                for x in understand[m]:
                    if(read_and_understand[x]==0):
                        tmp = False
                        break
                if(tmp):
                    read_and_understand[m]=1
        num+=1
        #print(*read_and_understand)
        if(prev.count(1)==read_and_understand.count(1)):
            print(-1)
            ans.append(-1)
            break
        prev = read_and_understand.copy()
        if(read_and_understand.count(0) == 1):
            print(num)
            ans.append(num)
            break

#print(*ans)