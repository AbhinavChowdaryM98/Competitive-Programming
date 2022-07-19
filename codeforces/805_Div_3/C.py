t = int(input())

for i in range(t):
    empty = input()
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a_dict = {}
    for j in range(n):
        try:
            a_dict[a[j]].append(j)
        except:
            a_dict[a[j]] = [j]
    for j in range(k):
        a,b = list(map(int, input().split()))
        try:
            if(a_dict[a][0] < a_dict[b][-1]):
                print("Yes")
            else:
                print("No")
        except:
            print("No")