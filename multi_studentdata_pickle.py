import pickle
fl=open('sdata.dat','wb')
l1=[]
l2=[]
n=int(input('ENTER THE NO.OF STUDENTS WHOSE DATA IS TO BE ENTERED:'))
for i in range(n):
    print('student no.',i+1)
    roll=int(input('enter the roll.no of student'))
    l1.append(roll)
    name=input('enter the name of the student')
    l2.append(name)    
dt={'ROLL':l1,'NAME':l2}    
pickle.dump(dt,fl)
fl.close()
f2=open('sdata.dat','rb')
d1=pickle.load(f2)
print('DATA:')
roll=d1['ROLL']
name=d1['NAME']
for i in range(len(roll)):
    print(roll[i],(':'),name[i])
f2.close()
