import pickle
fl=open('sdata.dat','wb')
roll=int(input('enter your roll.no'))
name=input('enter your name')
dt={'ROLL':roll,'NAME':name}
pickle.dump(dt,fl)
fl.close()
f2=open('sdata.dat','rb')
d1=pickle.load(f2)
print('output:')
print(d1)
f2.close()
