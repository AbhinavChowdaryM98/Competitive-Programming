t = int(input())

for i in range(t):
    x,y = input().split(" ")
    x,y = int(x), int(y)
    string = input()
    indices = []
    for j in range(30):
        if(string[j] == "0"):
            indices.append(j)
    val = [ indices[z+1]-indices[z]-1 for z in range(len(indices)-1)]
    if(string[-1]!="0"):
        val.append(30 - indices[-1] - 1)
    if(string[0]!="0"):
        val.insert(0, indices[0])
    ans = (30 -len(indices))*x + max(val)*y
    #print(val)
    print(ans)