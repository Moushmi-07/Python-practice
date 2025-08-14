#write a menu driven program to creat a binary file with employee id name
#designation salary department.input an employee no and update his salary.create display update and display and exit
import pickle
def creat():
    f=open("emplydata.dat",'wb')
    ch='y'
    while ch=='y':
        name=input('enter employe name')
        empid=int(input('enter employe id number.'))
        desig=input('enter designation')
        salary=int(input('enter the salary'))
        depart=input('Enter the department')
        data={'empid':empid,'name':name,'desig':desig,'salary':salary,'depart':depart}
       
        pickle.dump(data,f)
        ch=input('do you want add more? y/n')
    
    print('{:^80}'.format('file created'))
    f.close()
def read():
    f=open("emplydata.dat",'rb')
    print(('{:^10}{:^20}{:^10}{:^20}{:^10}').format('EMPLOYE ID','NAME','DESIGNATION','SALARY','DEPARTMENT'))
    
    while True:
        try:
            data=pickle.load(f)
            print(('{:^10}{:^20}{:^10}{:^20}{:^10}').format(data['empid'],data['name'],data['desig'],data['salary'],data['depart']))
        except EOFError:
            break
    f.close()
def update():
    f=open("emplydata.dat",'rb')
    empid=int(input('enter the employe id whose salary to be updated'))
    sal=int(input('enter the updated salary'))

    updata=[]
    v=True
    while True:
        try:
            udata=pickle.load(f)
            if udata['empid']==empid:
                udata['salary']=sal
                
                print('record after updation \n')
                print('EMPLOYE ID:',udata['empid'],'\n',
                      'NAME:',udata['name'],'\n',
                      'DESIGNATION:',udata['desig'],'\n',
                      'SALARY:',udata['salary'],'\n',
                      'DEPARTMENT:',udata['depart'])
                v=False
            updata.append(udata)    
                
        except EOFError:
            break
    if v==True:
        print('record not found.incorrect id number.try again')
    f.close()
    f=open("emplydata.dat",'wb')
    for i in updata:
        pickle.dump(i,f)
   
    print('\n file updated')
    f.close()

    
ch1='y'
print('''ENTER
          1 FOR CREATING A FILE 
          2 FOR DISPLAYING THE FILE
          3 FOR UPDATING THE SALARY OF AN EMPLOYEE
          4 FOR EXIT''')
while ch1=='y':
    
    print('')
    ch2=int(input('enter your choice '))
    if ch2==1:
        creat()
    if ch2==2:
        read()
    if ch2==3:
        update()
    if ch2==4:
        print('THANK YOU')
        break
    print('')
    ch1=input('do you want to continue? y for yes,n for no')
else:
    print('THANK YOU')

