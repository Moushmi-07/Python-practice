import pickle
##f1=open('studatas.dat','ab')
##ch=1
##while ch==1:
##    rn=int(input('enter your roll number'))
##    nm=input('enter your name')
##    per=int(input('enter your percentage'))
##    dt={'ROLL':rn,'NAME':nm,'PERCENTAGE':per}
##    pickle.dump(dt,f1)
##    ch=int(input('choise for next record(1-yes,2-no)'))
##    if ch==2:
##        break
##f1.close()
f2=open('studatas.dat','rb')
dt=pickle.load(f2)
print('data:',dt)
f2.close()
