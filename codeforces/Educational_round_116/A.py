t = int(input())
for i in range(t):
    s = input()
    if(len(s)==1):
        print(s)
    elif(s[0]==s[-1]):
        print(s)
    else:
        '''
        front = 0
        while(s[front]==s[front+1]):
            front+=1
        back = 0
        while(s[len(s)-1-back]==s[len(s)-2-back]):
            back+=1
            if(back>front):
                break
        if(front>back):
            tmp_s = s[0:len(s)-1-back]
            for j in range(len(s)-1-back, len(s)):
                tmp_s+=s[0]
            print(tmp_s)
        else:
            tmp_s = ""
            for j in range(front+1):
                tmp_s += s[-1]
            tmp2 = s[front+1:]
            tmp_s+=tmp2
            print(tmp_s)'''
        min = len(s)
        tmp = (0, len(s)-1)
        for j in range(len(s)):
            min_i = j
            min_j = j+1
            min_len = 1
            while(min_j<len(s)-1 and s[j]==s[min_j]):
                min_j+=1
                min_len+=1
            j = min_j
            if(min > min_len):
                min = min_len
                tmp = (min_i, min_j)
        tmp_s = s[0:tmp[0]]
        for j in range(tmp[0], tmp[1]):
            if(tmp[0]!=0):
                tmp_s += s[tmp[0]-1]
            else:
                tmp_s += s[tmp[1]]
        tmp_s += s[tmp[1]:]
        print(tmp_s)