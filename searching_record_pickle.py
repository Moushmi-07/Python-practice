import pickle
value=False
f1=open('studatas.dat','rb')
roll2=int(input('enter the roll numbrt to be searched'))
while True:
    try:
        rec=pickle.load(f1)
        if roll2==rec['ROLL']:
            print('record found')
            print('NAME=',rec['NAME'])
            print('ROLL=',rec['PERCENTAGE'])
            value=True
    except EOFError:
        break
if value==False:
    print('record not found')
f1.close()        

