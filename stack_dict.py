global d
d={}
global s
s=[]

def create():
    global d
    name=input('enter the name')
    mark=int(input('enter the mark'))
    d[name]=mark
def push():
    for i in d:
        if d[i]>75:
            s.append(i)
    print('record of students who scored above 75 has been pushed to stack')
def topop():
    if s==[]:
        print('stack is empty')
    else:
        print('the element popped is',s.pop())
def display():
    if s==[]:
        print('stack is empty')
    else:
        for i in range(len(s)-1,-1,-1):
         print(s[i])
        

    
c='y'
while c=='y':
    print('1.create\n 2.push\n 3.pop\n 4.display')
    ch=int(input('enter your choice'))
    if ch==1:
        create()
    elif ch==2:
        push()
    elif ch==3:
        topop()
    elif ch==4:
        display()


    c=input('do u want to continue y/n')
    
    
