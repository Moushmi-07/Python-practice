import csv
r=['1','aaaa','1200']
f=open('trial3.csv','w',newline='')
w=csv.writer(f)
w.writerow(r)
f.close()
with open('trial3.csv')as file:
    read=csv.reader(file,delimiter=',')
    print('{:^12}{:^10}{:^12}'.format('S.NO','NAME','SALARY'))
    print("==================================")
    for i in read:
        print('{:^12}{:^10}{:^12}'.format(i[0],i[1],i[2]))
        print('''

                  ''')
r2=[['2','bbbb','1300'],['3','cccc','1400']]
f2=open('trial3.csv','a',newline='')
w2=csv.writer(f2)
w2.writerows(r2)
f2.close()
with open('trial3.csv')as file:
    read=csv.reader(file,delimiter=',')
    print('{:^12}{:^10}{:^12}'.format('S.NO','NAME','SALARY'))
    print("==================================")
    for i in read:
        print('{:^12}{:^10}{:^12}'.format(i[0],i[1],i[2]))
