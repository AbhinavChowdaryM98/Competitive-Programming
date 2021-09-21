t = int(input().strip())

for i in range(t):
    l = input().split(" ")
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])
    if(a>b):
        tmp = a
        a = b
        b = tmp
    if(b>c):
        tmp = b
        b = c
        c = tmp
    if(a>c):
        tmp = a
        a = c
        c = tmp
    m = int(l[3])
    max_m = a + b + c - 3
    min_m = 0
    if(a!=b):
        tmp_a = a
        tmp_b = b
        tmp_c = c
        tmp_max_gap = tmp_c - 1
        tmp_fill1 = int(tmp_max_gap/2)
        tmp_fill2 = tmp_max_gap - tmp_fill1
        tmp_a -= tmp_fill1
        tmp_b -= tmp_fill2
        if abs(tmp_b - tmp_a) > 2:
            min_m = abs(tmp_b - tmp_a) - 2
    if m >= min_m and m <= max_m:
        if (m - min_m)%2 == 1:
            print("Yes")
        elif m == min_m or m == max_m:
            print("Yes")
        else:
            print("No")
    else:
        print("No") 