# l = "abcdefghijklmnopqrstuvwxyz"
# l = list(l)

# d = {}

# for i in range(26):
#     d[l[i]] = i+1

d_vowels = {"a": 1, "e": 5, "i": 9, "o": 15, "u": 21}
mid = list("cglr")
m = 1000000007

def mod(n):
    i = 1
    for j in range(n):
        # print(i)
        i = ((i*2)%m)
        # print(i)
    return i

t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    tmp = 0
    for j in s:
        if j not in d_vowels.keys():
            if j in mid:
                tmp+=1
    print(mod(tmp))