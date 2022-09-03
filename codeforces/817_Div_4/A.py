t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    if(n == 5):
        s.sort()
        name = ['T', 'i', 'm', 'r', 'u']
        if(name == s):
            print("Yes")
        else:
            print("No")
    else:
        print("No")