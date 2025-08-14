file=open('poem.txt','r')
str=file.read()
print(str)
count=0
for i in str:
    for j in str[1::]:
        if i.isalpha()!=True and j.isalpha==True :
            count+=1
print(count)        
file.close()
