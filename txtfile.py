file=open('poem.txt','w')
txt='''OVER hill, over dale
a
b'''
file.write(txt)
file.close()
file=open('poem.txt','r')
x=file.read()
y=x[0:3]
print(file.tell())
print(y)
file.close()


