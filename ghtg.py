a={'ram':{'maths':80,'english':90,'computer':85,'average':85},'shyam':{'maths':90,'english':95,'computer':100,'average':95},'mohan':{'maths':70,'english':80,'computer':75,'average':75}}
for i in a:
    print("name:",i)
    for x in i:
        print('marks:',i[x])
