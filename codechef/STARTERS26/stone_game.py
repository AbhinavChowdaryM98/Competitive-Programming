t = int(input())

for i in range(t):
    n = int(input())
    alice = list(input())
    bob = list(input())
    alice.sort()
    bob.sort(reverse=True)
    s = ['' for j in range(2*n)]
    back = 2*n - 1
    front = 0
    for j in range(2*n):
        if(j%2==0):
            if(alice[0] < bob[0]):
                s[front] += alice[0]
                alice.pop(0)
                front += 1
            else:
                s[back] += alice[-1]
                alice.pop()
                back-=1
        else:
            if(j < 2*n-1 and alice[0] < bob[0]):
                s[front] += bob[0]
                bob.pop(0)
                front+=1
            else:
                s[back] += bob[-1]
                bob.pop()
                back -= 1
    string = ''.join(s)
    print(string)