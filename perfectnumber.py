def number(num):
    sum=0
    for i in range(1,num):
        if i%num==0:
            sum+=i
    if sum==num:
        print('it is perfect no')
    else:
        print('no')
number(int(input('enter the number')))        
