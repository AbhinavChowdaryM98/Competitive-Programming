t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    one = s.count("1")
    if(one <= n//2):
        print("0"*(n-one))
    else:
        print("1"*one)