def bin_search(a, b):
    l = 0
    r = len(a)-1
    mid = (r+l)//2
    print(l,r,mid)
    while(l < r):
        if(a[mid] < b):
            l = mid+1
        elif(a[mid] > b):
            r = mid - 1
        else:
            return True
        mid = (r+l)//2
    return False

A = [20, 21, 44, 48, 62, 64, 65, 73, 77]

b = 59

print(bin_search(A,b))
