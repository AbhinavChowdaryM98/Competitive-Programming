t = int(input())

for i in range(t):
    n = int(input())
    init = list(map(int, input().split()))
    ans = []
    for j in range(n):
        tmp_n, s = input().split()
        d = list(s).count("D")
        u = int(tmp_n) - d
        tmp = init[j] - u + d
        # print(tmp)
        if(tmp > 9):
            tmp = tmp%10
        else:
            while(tmp<0):
                tmp+=10
        # print(tmp, end=" ")
        ans.append(tmp)
    print(*ans)