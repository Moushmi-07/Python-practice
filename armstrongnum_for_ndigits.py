def armstrong(num):
    sum=0
    a=str(num)
    n=len(a)
    for i in range(0,n):
        b=int(a[i])
        sum+=b**n
    if sum==num:
        print('the given number is an armstrong number')
    else :
        print('the given number is not an armstrong number')

    
    
    
