def swap(num,n):
    n=len(num)
    if n%2!=0:
        n-=1
    for i in range(0,n,2):
        j=i+1
        num[i],num[j]=num[j],num[i]
    print(num)
swap(eval(input('enter the list')),0)
def Awords():
    string=input('enter the text')
    words=string.split()
    total=0
    for i in words:
        if i[0]=='a' or i[0]=='A':
            total+=1
    print('no.of words starting with a or A are: ',total)
Awords()    
def prime():
    list=eval(input('eter the list'))
    n=len(list)
    for i in range(0,n):
        if list[i]==1:
            continue
        f=0
        for j in range(2,list[i]):
            if list[i]%j==0:
                f+=1
                break
        for x in range(0,1):
            if list[i]==2:
                list[i]=0
            if f==0:
                list[i]=0
    print(list)
prime()

def case():
    string=input('enter the text')
    words=string.split()
    print('{:^20}{:^40}{:^20}'.format('words','capital','small'))
    for i in words:
        caps=0
        small=0
        for j in i:
            if j.isupper()==True:
                caps+=1
            if j.islower()==True:
                small+=1
        for x in range(1):
            print('{:^20}{:^40}{:^20}'.format(i,caps,small))
case()     
def maxmin():
    list=eval(input('enter the list to find max and min value'))
    highest=list[0]
    lowest=list[0]
    for i in range (0,len(list)-1):
        if list[i]>highest:
            highest=list[i]
        if list[i]<lowest:
            lowest=list[i]
    print(' highest:',highest,'\n','lowest:',lowest)
        
maxmin()
while ch1==1:
    ch2=int(input('1.swap every alternate number'))
