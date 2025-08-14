a=[]
c='y'
while c=='y':
    print('1.insert')
    print('2.delete')
    print('3.display')
    print('4.exit')
    choice=eval(input('enter your choice'))
    if (choice==1):
        num=input('enter new number')
        a.append(num)
    elif(choice==2):
        if a==[]:
            print('queue empty')
        else:
            print('delete element is:',a[0])
            del a[0]
    elif choice==3:
        l=len(a)
        for i in range(0,l):
            print(a[i])
    elif choice==4:
        break
    else:
        print('wrong input')
        c=input('do you want to continue?(y/n)')
