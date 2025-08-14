import pickle
f1=open('studatas.dat','rb')
##print('records are')
##print('{:>20} {:^10} {:<20}'.format('ROLL','NAME','PERCENTAGE'))
while True:
    try:
        dt=pickle.load(f1)
        print('{:>12} {:^1} {:<12}'.format(dt['ROLL'],dt['NAME'],dt['PERCENTAGE']))
    except EOFError:
        break
f1.close()    
