t = int(input())

for i in range(t):
    n,x = input().split(" ")
    print(int(x)%(int(n)+1))
