import pickle
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
        
    for i in range(len(data)):
            if data[i]['ROLL']==roll:
                print('data before modification:',data[i])
                data[i]['MARK']=mark
                print('data after modification:',data[i])
    f.close()
    f1=open('studentdata.dat','wb')
    for x in data:
        pickle.dump(x,f1)
    print('')
    print('succesfully modified')     
    f1.close()
mdata()    
