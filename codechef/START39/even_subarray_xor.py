t = int(input())

for i in range(t):
    n = int(input())
    cpy = n
    p = 0
    while(cpy != 0):
        cpy = cpy//2
        p+=1
    a = [j for j in range(2,n+2)]
    start = 2**p
    print("start:", start)
    if(a[-1]-1 == start/2):
        start = start//2
        start += 2
    elif a[-1] == start:
        start+=2
    b = [start + j for j in range(n)]
    # for j in range(n):
    #     if j%2 == 0:
    #         if j != n-1:
    #             b[j] = a[j+1]
    #         else:
    #             b[j] = a[j] + 1
    #     else:
    #         b[j] = a[j-1]
    
    
    # s = a[0]
    # for j in range(1,n):
    #     s = s ^ a[j]
    #     if(j%2 == 1):
    #         print(j+1, "th :", s)
    # s = b[0]
    # for j in range(1,n):
    #     s = s ^ b[j]
    #     if(j%2 == 1):
    #         print(j+1, "th :", s)
    # print(*a)
    # print(*b)
    print(a[-1], b[0], b[-1])