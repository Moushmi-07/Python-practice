#create a binary file that stores information about students like roll no,name, marks in 3 subjects,and total.
#write a function to search the given roll no. and display the details of the students, if not found display appropriate message
#menu create display search exit.
import pickle
def creat():
    f=open("studata.dat",'wb')
    ch='y'
    while ch=='y':
        name=input('enter your name')
        rollno=int(input('enter your roll no.'))
        sst=int(input('enter your sst science marks'))
        eng=int(input('enter your eng marks'))
        maths=int(input('Enter your maths mark'))
        total=maths+sst+eng
        data={'name':name,'roln':rollno,'math':maths,'sst':sst,'eng':eng,'total':total}
        pickle.dump(data,f)
        ch=input('do you want add more? y/n')
    
    print('{:^80}'.format('file created'))
    f.close()

def read():
    f=open("studata.dat",'rb')
    print('{:^10}{:^20}{:^10}{:^20}{:^10}{:^20}'.format('NAME','ROLL NO','MATHS','sst','eng','TOTAL'))
    
    while True:
        try:
            data=pickle.load(f)
            print(('{:^10}{:^20}{:^10}{:^20}{:^10}{:^20}').format(data['name'],data['roln'],data['math'],data['sst'],data['eng'],data['total']))
        except EOFError:
            break
    f.close()
def search():
    f=open("studata.dat",'rb')
    n=int(input('ENTER THE STUDENTS ROLL NUMBER '))
    while True:
        try:
            data=pickle.load(f)
            if data['roln']==n:
                print(('{:^80}').format('RECORD FOUND'))
                print('')
                print('NAME:',data['name'])
                print('ROLL NUMBER:',data['roln'])
                print('MATHS:',data['math'])
                print('eng:',data['sst'])
                print('eng:',data['eng'])
                print('TOTAL:',data['total'])
                
                break
        except EOFError:
            print('record not found.try again')
            break
    f.close()
ch1='y'
print('''ENTER
          1 FOR CREATING A FILE 
          2 FOR DISPLAYING THE FILE
          3 FOR SEARCHING A STUDENT'S DETAIL
          4 FOR EXIT''')
while ch1=='y':
    
    print('')
    ch2=int(input('enter YOUR choice'))
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
    ch1=input('do you want to continue? y /n' )
else:
    print('THANK YOU')
    

    


    
        
