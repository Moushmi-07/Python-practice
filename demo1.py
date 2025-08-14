import pickle
f=open('poem.dat','rb')
f.seek(5,0)
x=pickle.load(f)

print(x)

print(f.tell())
##pickle.dump('''hello how are u
##this is moushmi
##now cs practical
##good bye''',f)
f.close()

