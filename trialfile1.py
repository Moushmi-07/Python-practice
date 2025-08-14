import csv
with open('trial2.csv')as file:
    read=csv.reader(file,delimiter=',')
    print('{:^12}{:^10}{:^12}'.format('S.NO','NAME','SALARY'))
    print("==================================")
    for i in read:
        print('{:^12}{:^10}{:^12}'.format(i[0],i[1],i[2]))
    
