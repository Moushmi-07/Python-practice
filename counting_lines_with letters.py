file=open('Country.txt','w')
txt='''whose woods these are i think i know.
his house is in the village though;
he will not see me stopping here
to watch his woods fill up with snow'''
file.write(txt)
file.close()
file=open('Country.txt','r')
x=file.readlines()
print(x)
w=0
h=0
for i in x:
    if i[0]=='w' or 'W':
        w+=1
    elif i[0]=='h' or 'H' :
        h+=1
print('W or w :',w)
print('H or h :',h)
file.close()

    
