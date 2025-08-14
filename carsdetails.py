import pickle
#accepting data
def wdata():
    f=open('cars.dat','ab')
    ch=1
    while ch==1:
        name=input('entre the car name')
        price=int(input('entre the price of the car'))
        milage=int(input('entre the milage'))
        series=int(input('entre the series'))
        data={'name':name,'price':price,'milage':milage,'series':series}
        pickle.dump(data,f)
        ch=int(input('do you want to entre datas, 1-yes,2-no'))
    f.close()
#reading data    
def rdata():
    f=open('cars.dat','rb')
    print('{:^12}{:^10}{:^12}{:>15}'.format('NAME','PRICE','MILAGE','SERIES'))
    while True:
        try:
            x=pickle.load(f)
            print('{:^12}{:^10}{:^12}{:>15}'.format(x['name'],x['price'],x['milage'],x['series']))
        except EOFError:
            break
    f.close()
#searching data
def sdata():
    ch=1
    while ch==1:
        f=open('cars.dat','rb')
        info=int(input('entre the car series to be searched'))
        value=False
        while True:
            try:
                x=pickle.load(f)
                if x['series']==info:
                    print('record found')
                    print('{:^12}{:^10}{:^12}{:^20}'.format('NAME','PRICE','MILAGE','SERIES'))
                    print('{:^12}{:^10}{:^12}{:^20}'.format(x['name'],x['price'],x['milage'],x['series']))
                    value=True
            except EOFError:
                break
        if value==False:
            print('record not found')
        f.close()
        ch=int(input('DO YOU WANT TO CONTINUE SEARCHING? 1-YES,2-EXIT'))
#modifing data
def mdata():
    f=open('cars.dat','rb')
    data=[]
    info=int(input('entre the series of car thats data to be modified'))
    mod=int(input('which data is to be modified? 1 for price, 2 for milage ,3 for name'))
    if mod==1 or mod==2:
        new=int(input('entre the new data'))
    elif mod==3:
        new=input('entre the new name')
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break
    value=False    
    for i in range(len(data)):
            if data[i]['series']==info:
                print('data before modification:',data[i])
                if mod==1:
                    data[i]['price']=new
                elif mod==2:
                    data[i]['milage']=new
                elif mod==3:
                    data[i]['name']=new
                else:
                    print('invalid input')
                print('data after modification:',data[i])
                value=True
    if value==False:
        print('the car doesnot exist in the file')
    f.close()
    f1=open('cars.dat','wb')
    for x in data:
        pickle.dump(x,f1)
    if value==True:
        print('')
        print('succesfully modified')
    f1.close()
                
#deleting data
def ddata():
    f = open('cars.dat','rb')
    info=input('entre the name of car thats detailes to be delted')
    data = []
    while True:
        try:
           rec = pickle.load(f)
           data.append(rec)
        except EOFError:
            break
    f.close()
    f = open('cars.dat','wb')
    for x in data:
        if x['name']==info:
            print('')
            print('succesfully deleted')
            continue
        pickle.dump(x,f)
    f.close()    
while True:
    print(' ')
    print('''CHOOSE
1 FOR WRITING DATA
2 FOR MODIFYING A DATA
3 FOR DELETING A DATA
4 FOR SEARCHING DATA
5 FOR DISPLAYING DATA
6 FOR EXITING''')
    choice=int(input('choose 1,2,3,4,5 or 6 according to previous information'))
    if choice==1:
        wdata()
    elif choice==2:
        mdata()
    elif choice==3:
        ddata()
    elif choice==4:
        sdata()
    elif choice==5:
        rdata()
    elif choice==6:
        print(' ')
        print('{:^50}'.format('THANK YOU'))
        break
    else:
        print(' ')
        print('invalid choice,try again')

