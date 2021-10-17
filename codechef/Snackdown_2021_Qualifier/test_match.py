t = int(input())

for i in range(t):
    tmp = input().split(" ")
    cnt = [tmp.count("0"), tmp.count("1"), tmp.count("2")]
    if(cnt[1]==cnt[2]):
        print("Draw")
    elif cnt[1]>cnt[2]:
        print("India")
    else:
        print("England")