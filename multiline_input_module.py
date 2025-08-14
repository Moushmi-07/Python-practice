#to take multiplelines as input
def multilinefor():
    n=int(input('ENTER THE NO. OF LINES YOU WANT TO ADD'))
    txt=''
    for i in range(n):
        print('enter your txt line by line')
        print('line',i+1,':')
        txt1=input()
        txt+=txt1
        txt+='\n'
    return txt
def multilinewhile():
    ch=True
    i=1
    txt=''
    print('enter your txt line by line')
    print('ENTER "n" if no more lines to be added ')
    while True:
        print('LINE.',i)
        ch=input('')
        if ch=='n':
            break
        i+=1
        txt+=ch
        txt+='\n'
    return txt

