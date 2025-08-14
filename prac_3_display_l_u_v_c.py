#write a program to count and display the number of lower case,upper case, vowels and consonents
def creat():
    f=open('myfile.txt','w')
    txt=input('enter your text')
    f.write(txt)
    f.close()
def read():
    f=open('myfile.txt','r')
    txt=f.readlines()
    print(txt)
    f.close()
def find():
    f1=open('myfile.txt','r')
    c,v,u,l=0,0,0,0
    txt1=f1.readlines()
    for i in txt1:
        w=i.split()
        for j in w:
            for x in j:
                if x in ['a','e','i','o','u','A','E','I','O','U'] :
                    v+=1
                if x not in ['a','e','i','o','u','A','E','I','O','U']:
                    c+=1
                if x.islower()==True:
                    l+=1
                if x.isupper()==True:
                    u+=1
    print('''WHAT DO YOU WANT TO FIND?
1 FOR NO.OF UPPER CASE CHARACTERS
2 FOR NO.OF LOWER CASE CHARACTER
3 FOR NO.OF VOWEL LETTERS
4 FOR NO.OF CONSONANTS
5 FOR ALL''')
    ch1=int(input('enter ur choice:'))
    if ch1==1:
        print('THE NO. OF UPPER CASE CHARACTERS IN THE TEXT FILE IS:',u)
        
    if ch1==2:
        print('THE NO.OF LOWER CASE CHARACTERS IN THE TEXT FILE IS:',l)
    if ch1==3:
        print('THE NO.OF VOWEL LETTER IN THE TEXT FILE IS:',v)
    if ch1==4:
        print('THE NO.OF CONSONANTS IN THE TEXT FILE IS:',c)
    if ch1==5:
        print('{:^20}{:^10}{:^10}{:^20}'.format('lower','upper','vowels','consonants'))
        print('{:^20}{:^20}{:^10}{:^20}'.format(l,u,v,c))
    f1.close()            
       
ch1='y'
while ch1=='y':
    print('''ENTER
                1 FOR CREATING A TEXT FILE
                2 FOR READING THE FILE
                3 FOR FINDING HOW MANY UPPERCASE,LOWERCASE,
                VOWELS AND CONSONANTS ARE PRESENT
                4 FOR EXIT''') 
    print('')
    ch2=int(input('enter your choice:'))
    if ch2==1:
        creat()
    if ch2==2:
        read()
    if ch2==3:
        find()
    if ch2==4:
        print('THANK YOU')
        break
    print('')
    ch1=input('do you want to continue? y for yes,n for no')
else:
    print('THANK YOU')


