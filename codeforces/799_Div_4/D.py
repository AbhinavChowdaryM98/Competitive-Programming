def check_palindrome(a):
    flag = True
    for i in range(len(a)//2):
        if(a[i] != a[len(a)-i-1]):
            flag = False
            break
    return flag

def make_time(h,m):
    p = ""
    if(h<10):
        p+= "0"
    p+= str(h)
    p+=":"
    if(m<10):
        p+= "0"
    p+=str(m)
    return p

def extract_time(p):
    h,m = list(map(int, p.split(":")))
    return h,m

def add_time(p, x):
    h,m = extract_time(p)
    h += x//60
    m += x%60
    h += m//60
    m = m%60
    h = h%24
    return make_time(h,m)


t = int(input())

for i in range(t):
    s,x = input().split()
    x = int(x)
    ans = 0
    if(check_palindrome(s)):
        ans+=1
    p = add_time(s,x)
    while(p!=s):
        if(check_palindrome(p)):
            ans+=1
        p = add_time(p, x)
        # print(p)
    print(ans)