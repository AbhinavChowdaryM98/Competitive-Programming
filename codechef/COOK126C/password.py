t = int(input().strip())

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

digits = '0123456789'

characters = ['@', '#', '%', '&', '?']

for i in range(t):
    tmp_string = input()
    #print(len(tmp_string))
    if(len(tmp_string)<10):
        print("NO")
        continue
    else:
        check = {'lower':False,'upper':False,'digit':False,'character':False}
        length = len(tmp_string)
        for j in range(length):
            if tmp_string[j] in list(ascii_lowercase):
                check['lower'] = True
            if tmp_string[j] in list(ascii_uppercase):
                if j!=length-1 and j!=0:
                    check['upper'] = True
            if tmp_string[j] in list(digits):
                if j!=0 and j!=length-1:
                    check['digit'] = True
            if tmp_string[j] in characters:
                if j!=length-1 and j!=0:
                    check['character'] = True
        if((check['lower'] and check['upper']) and (check['digit'] and check['character'])):
            print("YES")
        else:
            print("NO")