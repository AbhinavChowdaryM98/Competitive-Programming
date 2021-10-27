t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(lambda x: int(x), input().split(" ")))
    possible = []
    ans = 0
    for j in range(n):
        tmp_poss = 0
        if(j+1>=arr[j]):
            l = j+1-arr[j]
            prev = 1
            if((l,j) not in possible):
                possible.append((j,j))
                tmp_poss+=1
            for r in range(j+1, n):
                if((l,r) in possible):
                    break
                else:
                    possible.append((l,r))
                    if(arr[r] == r+1-l):
                        prev+=1
                    #print(prev)
                    tmp_poss += prev
        ans += tmp_poss
    #print(possible)
    print(ans)