t = int(input())

for i in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    flag = True
    for j in range(n):
        if(s1[j] == 'R' or s2[j] == 'R'):
            if(s1[j] != s2[j]):
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")