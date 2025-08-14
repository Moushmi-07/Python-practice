import pickle

#writing data
def wdata():
    f=open('studentdata.dat','ab')
    ch=int(input('start entering datas,1-ok,2-exit'))
    while ch==1:
        roll=int(input('entre the roll number'))
        name=input('entre the name')
        mark=int(input('entre the mark out of 100'))
        data={'ROLL':roll,'NAME':name,'MARK':mark}
        pickle.dump(data,f)
        ch=int(input('do you want to entre datas, 1-yes,2-no'))
    f.close()
    
#reading data    
def rdata():
    f=open('studentdata.dat','rb')
    print('{:^12}{:^10}{:^12}'.format('ROLL','NAME','MARK'))
    while True:
        try:
            x=pickle.load(f)
            print('{:^12}{:^10}{:^12}'.format(x['ROLL'],x['NAME'],x['MARK']))
        except EOFError:
            break
    f.close()
    
#searching data
def sdata():
    ch=1
    while ch==1:
        f=open('studentdata.dat','rb')
        info=int(input('entre the roll number to be searched'))
        value=False
        while True:
            try:
                x=pickle.load(f)
                if x['ROLL']==info:
                    print('record found')
                    print('{:^12}{:^10}{:^12}'.format('ROLL','NAME','MARK'))
                    print('{:^12}{:^10}{:^12}'.format(x['ROLL'],x['NAME'],x['MARK']))
                    value=True
            except EOFError:
                break
        if value==False:
            print('record not found')
        f.close()
        ch=int(input('DO YOU WANT TO CONTINUE SEARCHING? 1-YES,2-EXIT'))
        
#modifing data
def mdata():
    f=open('studentdata.dat','rb')
    data=[]
    roll=int(input('entre the roll no. of student whose data to be modified'))
    mark=int(input('entre the mark tat should be replaced in the entred roll no'))
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break
    value=False    
    for i in range(len(data)):
            if data[i]['ROLL']==roll:
                print('data before modification:',data[i])
                data[i]['MARK']=mark
                print('data after modification:',data[i])
                value=True
    if value==False:
        print('the roll number doesnot exist in the file')
    f.close()
    f1=open('studentdata.dat','wb')
    for x in data:
        pickle.dump(x,f1)
    if value==True:
        print('')
        print('succesfully modified')
    f1.close()
    
#deleting data

        
while True:
    print(' ')
    print('''CHOOSE 1 FOR WRITING DATA
2 FOR READIND DATA
3 FOR SEARCHING A DATA
4 FOR MODIYING A DATA
5 FOR DELETING DATA
6 FOR EXITING''')
    choice=int(input('choose 1,2,3,4,5 or 6 according to previous information'))
    if choice==1:
        wdata()
    elif choice==2:
        rdata()
    elif choice==3:
        sdata()
    elif choice==4:
        mdata()
    elif choice==5:
        ddata()
    elif choice==6:
        print(' ')
        print('{:^50}'.format('THANK YOU'))
        break
    else:
        print(' ')
        print('invalid choice,try again')
        
    
