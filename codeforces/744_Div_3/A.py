t = int(input())

for i in range(t):
    s = input()
    if(len(s)%2 == 1):
        print("No")
    else:
        tmp = list(s)
        b = tmp.count("B")
        a = tmp.count("A")
        c = tmp.count("C")
        if(b == a + c):
            print("Yes")
        else:
            print("No")