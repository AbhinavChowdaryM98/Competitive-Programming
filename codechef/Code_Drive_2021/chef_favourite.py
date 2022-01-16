t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    code = []
    chef = []
    for j in range(n):
        if(s[j]=="c"):
            if(s[j+1]=="o" and s[j+2]=="d" and s[j+3]=="e"):
                code.append(j)
            elif(s[j+1]=="h" and s[j+2]=="e" and s[j+3]=="f"):
                chef.append(j)
    if(code[0]<chef[0]):
        print("AC")
    else:
        print("WA")