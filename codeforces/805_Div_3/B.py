t = int(input())

for i in range(t):
    s = input()
    # n = set(list(s))
    # print(n)
    # print((len(n)+2)//3)
    tmp = []
    ans = 0
    for i in s:
        if(i not in tmp):
            if(len(tmp) == 3):
                tmp[0] = i
                del tmp[2]
                del tmp[1]
                ans+=1
            else:
                tmp.append(i)
    print(ans+1)