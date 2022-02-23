t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    '''
    dis = []
    for j in range(n):
        tmp = s[:j] + s[j+1:]
        dis.append(tmp)
    dis = set(dis)
    print(len(dis))'''
    changes = 0
    prev = s[0]
    for j in range(n):
        if(prev != s[j]):
            changes+=1
            prev = s[j]
    print(changes+1)