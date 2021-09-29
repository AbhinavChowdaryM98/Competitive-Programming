t = int(input())

for i in range(t):
    co_or = list(input().split(" "))
    if((int(co_or[0])+int(co_or[1]))%2 == 0):
        print("Yes")
    else:
        print("No")