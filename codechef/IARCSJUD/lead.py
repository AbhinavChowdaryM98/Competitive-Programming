t = int(input())
max_lead = -1
max_i = -1
for i in range(t):
    a,b = list(map(int, input().split()))
    if(b > a):
        if(max_lead < (b-a)):
            max_lead = b - a
            max_i = 2
    elif(a > b):
        if(max_lead < (a - b)):
            max_lead = a - b
            max_i = 1
print(max_i, max_lead)