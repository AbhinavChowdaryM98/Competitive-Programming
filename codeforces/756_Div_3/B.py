t = int(input())
for i in range(t):
    num = list(map(lambda x: int(x), input().split(" ")))
    a = min(num)
    b = max(num)
    if(a < int(b/3)):
        print(a)
    else:
        if(a==b):
            print(int(a/2))
        else:
            ans = int(a/2)
            cp_a = a - ans*2
            cp_b = b - ans*2
            if(cp_a != 0 and cp_b >= 3):
                ans+=1
                cp_a-=1
                cp_b-=3
            ans += int(cp_b/4)
            print(ans)