# write a program to read a text file line by line and display each word seperated by a hash
def d1():        
    f=open('poem.txt','r')
    l=f.readlines()
    for i in l:
        w=i.split()
        for x in w :
            print(x,end='#')
    f.close()       
def d2():
    f=open('poem.txt','r')
    txt=f.readlines()
    for i in txt:
        print(i)
    f.close()
def d3():
   f=open('poem.txt','w+')
   txt=input('enter the text')
   f.write(txt)
   f.close()
    
def exit():
    print('thank you')
ch=1

while ch==1:
    print('''ENTER
               1 to write into a file
               2 to read the file
               3 to display the text of the file seperated by hash
               4 to exit''')
    ch2=int(input('enter ur choice'))
    if ch2==1:
        d3()
    elif ch2==2:
        d2()
    elif ch2==3:
        d1()
        print('\n')
    elif ch2==4:
        exit()
        break
    else:
        print('invalid input try again')
    
    


