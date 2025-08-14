s=[]
c='y'
while (c=='y'):
    print('''1.push
    2.pop
    3.display''')
    choice=eval(input('enter your choice: '))
    if choice==1:
        a=input('enter any  number:')
        s.append(a)
    elif choice==2:
        if (s==[]):
            print('stack is empty')
        else:
            print('deleted element is:',s.pop())
        
    elif choice==3:
        if (s==[]):
            print('stack is empty')
        else:
            l=len(s)
            for i in range(l-1,-1,-1):
                print(s[i])
    else:
        print('wrong input')
        c=input('do you want to continue? (y/n)')
