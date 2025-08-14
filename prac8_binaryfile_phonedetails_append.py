#write a program to creat a binary file phone.dat that accepts details like phone number model strg cap display size etc .
#prg shld allow the user to append more records
import pickle
def apend():
    f=open('phone.dat','ab+')
    phno=int(input(' enter the phone number'))
    model=input('enter the model')
    strgcap=input('enter the storage capacity')
    dsply=input('enter the display size')
    data={'phno':phno,'model':model,'strgcap':strgcap,'dsply':dsply}
    pickle.dump(data,f)
    print('RECORD ADDED')
    f.close()
def read():
    f=open('phone.dat','rb')
    print('{:^15} {:^15} {:^15} {:^15}'.format('PHONE NUMBER','MODEL','STORAGE CAPACITY','DISPLAY SIZE'))
    while True:
        try:
            data=pickle.load(f)
            print('{:^15} {:^15} {:^15} {:^15}'.format(data['phno'],data['model'],data['strgcap'],data['dsply']))
        except EOFError:
            break      
def search():
    f=open('phone.dat','rb')
    i=int(input('enter the phone number'))
    
    while True:
        try:
            data=pickle.load(f)
            if data['phno']==i:
                print('\n #record found \n')
                print('PHONE NUMBER:',data['phno'])
                print('MODEL:',data['model'])
                print('STORAGE CAPACITY:',data['strgcap'])
                print('DISPLAY SIZE:',data['dsply'])
                break
        except EOFError:
            print('record not found')
            break
ch1='y'
while ch1=='y':
    print('''ENTER
          1 FOR ADDING DETAILS 
          2 FOR DISPLAYING THE FILE
          3 FOR SEARCHING A PHONE'S DETAILS
          4 FOR EXIT''')
    print('')
    ch2=int(input('enter your choice '))
    if ch2==1:
        apend()
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

