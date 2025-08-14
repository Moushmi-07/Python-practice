#write a program to remove all the lines that contain the charecter a in a file and write it to another file
import multiline_input_module as ml
def creat():
    f=open('myfile.txt','w')
    txt=ml.multilinewhile()
    print('file created')
    f.write(txt)
    f.close()
def read():
    print('''which file do u want to read?
          1. for existing file,
          2.for the new file after editing
          3.for both''')
    ch=int(input('ente ryour choice'))
    if ch==1:
        f1=open('myfile.txt','r')
        txt=f1.readlines()
        print('THE EXISTING FILE:\n',txt)
        f1.close()
    if ch==2:
        f2=open('newfile.txt','r')
        txt=f2.readlines()
        print('THE NEW FILE:\n',txt)
        f2.close()
    if ch==3:
        f1=open('myfile.txt','r')
        txt=f1.readlines()
        print('THE EXISTING FILE:\n',txt)
        f2=open('newfile.txt','r')
        txt1=f2.readlines()
        print('THE NEW FILE:\n',txt1)
        f1.close()
        f2.close()
        
def file():
    f1=open('myfile.txt','r')
    txt1=f1.readlines()
    rl=[]
    sl=[]
    for i in txt1:
        for j in i:
            if 'a'==j or 'A'==j:
                rl.append(i)
                break
        else:
            sl.append(i)
    

    f1.close()
    f2=open("myfile.txt",'w')
    f3=open('newfile.txt','w')
    for i in sl:
        f2.write(i)
    for j in rl:
        f3.write(j)
    print('\n file edited')
    f2.close()
    f3.close()
ch1='y'
print('''ENTER
          1 FOR CREATING FILE
          2 FOR DISPLAYING FILE
          3 FOR REMOVING LINES FROM A FILE THAT CONTAINS CHARACTER A
          AND ADD THOSE LINES IN NEW FILE
          4 FOR EXIT''')
while ch1=='y':
    
    print('')
    ch2=int(input('enter your choice'))
    if ch2==1:
        creat()
    if ch2==2:
        read()
    if ch2==3:
        file()
    if ch2==4:
        print('THANK YOU')
        break
    print('')
    ch1=input('do you want to continue? y for yes,n for no')
else:
    print('THANK YOU')
    
    

