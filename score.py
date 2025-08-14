import pickle
global name
name=input('enter player name')
score=0
def npreplayed():
    f=open('scoreboard.dat','ab+')
    
    d={'name':name,'hscore':score}
    print('hello',name.upper(),'find more number of words to get points and beat the scores of your friends')
    pickle.dump(d,f)
    f.close()
def preplayed():
    try:
        f=open('scoreboard.dat','rb')
    except FileNotFoundError:
            npreplayed()
            return 

    while True:
        try:
            data=pickle.load(f)
            if name.upper()==data['name'].upper():
                print('welcome back',name.upper(),'your highest score was',data['hscore'])
                f.close()
                break
            
                
        except EOFError:
            npreplayed()
            break
def sboard():
        f=open('scoreboard.dat','rb')
        print('{:^25}{:^50}'.format('NAME','HIGHEST SCORE'))
        while True:
            try:
                data=pickle.load(f)
                print('{:^25}{:^50}'.format(data['name'],data['hscore']))
            
            except EOFError:
                break
        
##        if preplayer==False:
##        
##            f1=open('scoreboard.dat','ab+')
##            d={'name':name,'hscore':0}
##            pickle.dump(d,f)
##            print('hello',name.upper(),'find more number of words to get points and beat your friends score')
##            f1.close()
##            break
##
##detail()
##d={name:score}
##pickle.dump(d,f)

##def update():
##    f=open("emplydata.dat",'rb')
##    empid=int(input('enter the employe id whose salary to be updated'))
##    sal=int(input('enter the updated salary'))
##
##    updata=[]
##    v=True
##    while True:
##        try:
##            udata=pickle.load(f)
##            if udata['empid']==empid:
##                udata['salary']=sal
##                
##                print('record after updation \n')
##                print('EMPLOYE ID:',udata['empid'],'\n',
##                      'NAME:',udata['name'],'\n',
##                      'DESIGNATION:',udata['desig'],'\n',
##                      'SALARY:',udata['salary'],'\n',
##                      'DEPARTMENT:',udata['depart'])
##                v=False
##            updata.append(udata)    
##                
##        except EOFError:
##            break
##    if v==True:
##        print('record not found.incorrect id number.try again')
##    f.close()
##    f=open("emplydata.dat",'wb')
##    for i in updata:
##        pickle.dump(i,f)
##   
##    print('\n file updated')
##    f.close()

    
