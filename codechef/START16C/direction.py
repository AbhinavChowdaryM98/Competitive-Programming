t = int(input())

dir = ["N", "E", "S", "W"]

for i in range(t):
    prof_dir = 0
    n = int(input())
    string = list(input())
    flag = False
    for j in range(len(string)-1):
        if(string[j]==string[j+1]):
            flag = True
            break
    if(flag):
        print("Yes")
    else:
        print("No")