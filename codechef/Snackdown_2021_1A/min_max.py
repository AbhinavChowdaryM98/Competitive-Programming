t = int(input())

for i in range(t):
    a,b = input().split(" ")
    a,b = int(a), int(b)
    minimum = 2*a
    maximum = (a*b)*(a*b-1)
    print(minimum, maximum)