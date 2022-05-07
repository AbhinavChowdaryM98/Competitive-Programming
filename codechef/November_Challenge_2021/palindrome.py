t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(lambda x: int(x), input().split(" ")))
    odds = []
    for j in num:
        if(j%2==1):
            odds.append(j)
    changes = 0
    if(len(odds)<2):
        print(changes)
    else:
        changes = int(len(odds)/2)
        print(changes)