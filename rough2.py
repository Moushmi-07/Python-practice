import pickle
def ddata(r):
     f = open('d:/student.dat','rb')
    reclst = []
    while True:
        try:
           rec = pickle.load(f)
           reclst.append(rec)
        except EOFError:
            break
    f.close()
    f = open('d:/student.dat','wb')
    for x in reclst:
        if x['Rollno']==r:
            continue
        pickle.dump(x,f)
    f.close()    
ddata()
