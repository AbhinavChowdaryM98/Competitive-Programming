def complement(s):
    if s == "U":
        return "D"
    elif s == "D":
        return "U"
    return s

t = int(input())

while(t>0):
    len = int(input())
    string = input()
    ans = ""
    for i in string:
        ans+=complement(i)
    print(ans)
    t-=1