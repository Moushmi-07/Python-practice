import math as m
def persqr():
    for i in range(1000,9999):
        x=m.sqrt(i)
        if m.ceil(x)==x:
            print(i,end=', ')
    

print('THE PERFECT SQARES THAT OCCURE IN THE RANGE 1000 TO 9999 ARE:')
print('\n')
persqr()

