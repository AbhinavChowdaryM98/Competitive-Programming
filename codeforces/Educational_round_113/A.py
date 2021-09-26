t = int(input())

for i in range(t):
    n = int(input())
    string = input()
    vis = [{'a':0, 'b':0} for i in range(n)]
    vis[0][string[0]]+=1
    for j in range(1,n):
        vis[j]['a'] = vis[j-1]['a']
        vis[j]['b'] = vis[j-1]['b']
        vis[j][string[j]] += 1
    a = -1
    b = -1
    #for z in vis:
        #print(z['a'], z['b'])
    for m in range(n):
        for x in range(m+1,n):
            tmp_a = vis[x]['a'] - vis[m]['a']
            tmp_b = vis[x]['b'] - vis[m]['b']
            if(string[m]=='a'):
                tmp_a+=1
            else:
                tmp_b+=1
            if(tmp_a==tmp_b):
                a = m + 1
                b = x + 1
                break
    print(a,b)