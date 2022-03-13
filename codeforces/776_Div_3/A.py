t = int(input())

for i in range(t):
    s = input()
    c = input()
    if(c not in s):
        print("NO")
    else:
        ind = s.index(c)
        cnt = s.count(c)
        if(ind%2 == 0):
            print("YES")
        else:
            if(cnt == 1):
                print("NO")
            else:
                flag = False
                for i in range(ind+1, len(s)):
                    if(s[i] == c):
                        if(i%2 == 0):
                            print("YES")
                            flag = True
                            break
                if(not flag):
                    print("NO")