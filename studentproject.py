import pickle

#Accepting data for Dictionary
def insertRec():
    rollno = int(input('Enter roll number:'))
    name = input('Enter Name:')
    marks = int(input('Enter Marks:'))

    #Creating the Dictionary
    rec = {'Rollno':rollno,'Name':name,'Marks':marks}

    #Writing the Dictionary
    f = open('student.dat','ab')
    pickle.dump(rec,f)
    f.close()

#Reading the records
def readRec():
    f = open('student.dat','rb')
    while True:
        try:
            rec = pickle.load(f)
            print('Roll Num:',rec['Rollno'])
            print('Name:',rec['Name'])
            print('Marks:',rec['Marks'])
        except EOFError:
            break
    f.close()

#Searching a record based on Rollno
def SearchRollno(r):
    f = open('student.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['Rollno']==r:
                print('Roll Num:',rec['Rollno'])
                print('Name:',rec['Name'])
                print('Marks:',rec['Marks'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('No Records found')
    f.close()

#Marks Modification for a RollNo
def updateMarks(r,m):
    f = open('student.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(reclst)):
        if reclst[i]['Rollno']==r:
            reclst[i]['Marks']= m
    f = open('student.dat','wb')
    for x in reclst:
        pickle.dump(x,f)
    f.close()

#Deleting a record based on Rollno
def deleteRec(r):
    f = open('student.dat','rb')
    reclst = []
    while True:
        try:
           rec = pickle.load(f)
           reclst.append(rec)
        except EOFError:
            break
    f.close()
    f = open('student.dat','wb')
    for x in reclst:
        if x['Rollno']==r:
            continue
        pickle.dump(x,f)
    f.close()
while True:
    print('Type 1 to insert rec')
    print('Type 2 to display rec')
    print('Type 3 to Search RollNo ')
    print('Type 4 to update marks')
    print('Type 5 to delete a Records')
    print('Enter your choice 0 to exit')
    choice = int(input('Enter your choice'))
    if choice == 0:
        break
    if choice == 1:
        insertRec()
    if choice == 2:
        readRec()
    if choice == 3:
        r = int(input('Enter a rollno to search:'))
        SearchRollno(r)
    if choice == 4:
        r = int(input('Enter a rollno:'))
        m = int(input('Enter new Marks:'))
        updateMarks(r,m)
    if choice == 5:
        r = int(input('Enter a rollno:'))
        deleteRec(r)
