t = int(input())

for i in range(t):
    a = input().split(" ")
    cnt0 = a.count("0")
    cnt1 = a.count("1")
    if(cnt1 > cnt0):
        print("Yes")
    else:
        print("No")