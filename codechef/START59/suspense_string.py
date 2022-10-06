# cook your dish here
t = int(input())

for i in range(t):
    ans = ""
    n = int(input())
    s = list(input())
    j = 0
    while(len(s) > 0):
        if(j%2 == 0):
            if(s[0] == "0"):
                ans = "0"+ans
            else:
                ans = ans+"1"
            del s[0]
        else:
            if(s[-1] == "1"):
                ans = "1" + ans
            else:
                ans = ans + "0"
            del s[len(s)-1]
        j+=1
    print(ans)