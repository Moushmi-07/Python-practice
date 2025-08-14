#creat a csv file tat stores user name and password.read and search the password for the given user name
import csv
def creat():
    with open('passwords.csv','w') as f:
        data=[]
        ch='y'
        while ch=='y':
            sdata=[]
            username=input('enter the user name')
            password=input('enter the password')
            sdata.append(username)
            sdata.append(password)
            data.append(sdata)
            ch=input(' do you want to add more?y/n')
        w=csv.writer(f,lineterminator='\n')
        w.writerows(data)
def read():
    with open('passwords.csv','r') as f:
        r=csv.reader(f)
        print('{:^20}{:^30}'.format('USERNAME','PASSWORD'))
        for i in r:
            print('{:^20}{:^55}'.format(i[0],i[1]))
def search():
    with open('passwords.csv','r') as f:
        r=csv.reader(f)
        username=input('ENTER THE USER NAME')
        v=False
        for i in r:
            if i[0]==username:
                print('password found\n')
                print('{:^20}{:^30}'.format('USERNAME','PASSWORD'))
                print('{:^20}{:^30}'.format(i[0],i[1]))
                v=True
                break
        if v==False:
            print('user name does not exist')
ch1='y'
while ch1=='y':
    print('''ENTER
          1 FOR CREATING A FILE 
          2 FOR DISPLAYING THE FILE
          3 FOR SEARCHING THE PASSWORD
          4 FOR EXIT''')
    print('')
    ch2=int(input('enter your choice '))
    if ch2==1:
        creat()
    if ch2==2:
        read()
    if ch2==3:
        search()
    if ch2==4:
        print('THANK YOU')
        break
    print('')
    ch1=input('do you want to continue? y for yes,n for no')
else:
    print('THANK YOU')
                
            

        
            
            
    
