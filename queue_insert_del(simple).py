import queue_module as q
c='y'
while c=='y':
    q.menu()
    choice=eval(input('enter your choice'))
    if choice==1:
        q.insert()
    elif choice==2:
        q.delete()
    elif choice==3:
        q.display()
    elif choice==4:
        q.exit()
        break
    c=input('do you want to continue?(y/n)')
    if c=='n':
        print('thank you')
