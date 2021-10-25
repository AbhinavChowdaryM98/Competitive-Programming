t = int(input())

for i in range(t):
    s = input()
    tmp = set(list(s))
    tmp = list(tmp)
    tmp.sort()
    char = tmp[0]
    ind = s.find(char)
    printer = ""
    for j in range(len(s)):
        if(j != ind):
            printer += s[j]
    print(char, printer)