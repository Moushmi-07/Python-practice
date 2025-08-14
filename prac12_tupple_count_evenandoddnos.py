even,odd=0,0
def tup1(t):
    for i in range(len(t)):
        global even
        global odd
        if t[i]%2==0:
            even+=1
        else:
            odd+=1
        
x=eval(input('enter a tuple'))
tup1(x)
print('NO.OF EVEN NUMBERS IN THE TUPPLE IS:',even,'\n',"NO.OF ODD NUMBERS IN THE TUPPLE IS:",odd)
