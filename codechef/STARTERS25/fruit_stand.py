t = int(input())

for i in range(t):
    x,y = input().split(" ")
    print(min(int(int(x)/2), int(y)))
