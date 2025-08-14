#write a program to accept vehical info like vehicle no. name, make,cost,performance using a binary file.
#search for a particular vehicle and delete the vehicles details from the file
import pickle
def creat():
    f=open('vehicles.dat','wb')
    ch='y'
    while ch=='y':
        vehno=input('enter the vehicle number')
        name=input('enter the vehicle name ')
        make=input('enter the vehicle make ')
        cost=int(input('enter the cost of the vehicle'))
        perf=input('enter the performance')
        data={'vehno':vehno,'name':name,'make':make,'cost':cost,'perf':perf}
        pickle.dump(data,f)
        ch=input('do you want to add more?y/n')
    print('\n #FILE CREATED#')
    f.close()
def read():
    f=open('vehicles.dat','rb')
    print('{:^10}{:^20}{:^10}{:^20}{:^10}'.format('VEHICLE NO.','NAME','MAKE','COST','PERFORMANCE'))
    while True:
        try:
            data=pickle.load(f)
            print('{:^10}{:^20}{:^10}{:^20}{:^10}'.format(data['vehno'],data['name'],data['make'],data['cost'],data['perf']))

        except EOFError:
            break
    f.close()
def delete():
    f=open('vehicles.dat','rb')
    vehnum=input('enter the vehicle number')
    data2=[]
    while True:
        try:
            data=pickle.load(f)
            data2.append(data)
        except EOFError:
            break
    f.close()
    for i in data2:
        if i['vehno']==vehnum:
                    print('\n')
                    print('{:^10}{:^20}{:^10}{:^20}{:^10}'.format('VEHICLE NO.','NAME','MAKE','COST','PERFORMANCE'))
                    print('{:^10}{:^20}{:^10}{:^20}{:^10}'.format(i['vehno'],i['name'],i['make'],i['cost'],i['perf']))
                    ch=input('\n DO YOU WANT TO DELETE THE ABOVE VEHICLE DETAILS?y/n')
                    if ch=='y':
                        data2.remove(i)
                        print('\n #RECORD DELETED#')
                        break
    f=open('vehicles.dat','wb')
    for x in data2:
        pickle.dump(x,f)
    f.close()
ch1='y'
while ch1=='y':
    print('''ENTER
          1 FOR CREATING A FILE 
          2 FOR DISPLAYING THE FILE
          3 FOR DELETING A VEHICLE'S DETAILS
          4 FOR EXIT''')
    print('')
    ch2=int(input('enter your choice '))
    if ch2==1:
        creat()
    if ch2==2:
        read()
    if ch2==3:
        delete()
    if ch2==4:
        print('THANK YOU')
        break
    print('')
    ch1=input('do you want to continue? y/n')
else:
    print('THANK YOU')

    
    
