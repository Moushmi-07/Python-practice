global s
s=[]
def create():
    global l
    l=eval(input('enterthe values in a list'))
def topush():
    
    for i in l:
        if i%2==0:
            s.append(i)
    print('even numbers are pushed to the stack')
def topop():
    
    if s==[]:
        print('stack is empty')
    else:
        print('the element poped is',s.pop)
def todisplay():
    
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
        topush()
    elif ch==3:
        topop()
    elif ch==4:
        todisplay()


    c=input('do u want to continue y/n')
    
    
