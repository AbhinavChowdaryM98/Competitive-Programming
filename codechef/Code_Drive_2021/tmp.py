from itertools import product

arr = list(product([0,1,2], repeat=2))
ans = 0
for l in arr:
    for i in range(1, 1):
        if(l[i]<l[i+1] and l[i]<l[i-1]):
            ans+=1
        elif(l[i]>l[i+1] and l[i]>l[i-1]):
            ans+=1
print(ans)