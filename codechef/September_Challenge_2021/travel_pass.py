t = int(input())

for i in range(t):
    tmp = input().split(" ")
    n = int(tmp[0])
    a = int(tmp[1])
    b = int(tmp[2])
    string = input()
    zeroes = string.count("0")
    ones = string.count("1")
    print(a*zeroes+b*ones)