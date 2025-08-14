
s=[]
c='y'
while c=='y':
    print('1.PUSH\n 2.POP\n 3.DISPLAY\n 4.PEEK')
    ch=eval(input('enter your choice: '))
    if ch==1:
        a=input('enter any number')
        s.append(a)
    elif ch==2:
        if s==[]:
            print('stack is empty / stack underflow')
        else:
            print('the element popped is',s.pop())
    elif ch==3:
        if s==[]:
            print('stack is empty / stack underflow')
        else:
            l=len(s)
            for i in range(l-1,-1,-1):
                print(s[i])
    elif ch==4:
        if s==[]:
            print('stack is empty / stack underflow')
        else:
            l=len(s)-1
            print('the elemnt peeked is',s[l])
    else:
        print('wrong input')
    c=input('do you want to continue..(y/n)')
            
