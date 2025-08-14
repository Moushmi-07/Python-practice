f=open('poem.txt','r')
txt=f.readlines()
count=0
for i in txt:
    word=i.split()
    if 'the' in word:
        count+=1
print(count)
