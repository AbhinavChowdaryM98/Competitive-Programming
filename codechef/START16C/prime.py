import math
import time
start = time.time()

arr = [1 for i in range(10000002)]
for i in range(2,int(math.sqrt(len(arr)))):
    for j in range(2, int(len(arr)/i)):
        arr[i*j] = 0

t = int(input())

for i in range(t):
    x,y = input().split(" ")
    x,y = int(x), int(y)
    ans = 0
    if(x%2 == 0):
        ans+=1
        x+=1
    while(x+2 <= y):
        if(arr[x+2]==1):
            ans+=1
        else:
            ans+=2
        x += 2
    if(x==y):
        print(ans)
    else:
        print(ans+1)

ending = time.time()

print(ending-start)