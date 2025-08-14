def emirp_number(num):
    factors_num,factors_rev=0,0
    a=str(num)
    rev=int(a[::-1])
    for i in range(1,num+1):
        if num%i==0:
            factors_num+=1
    for x in range(1,rev+1):
        if rev%x==0:
            factors_rev+=1
    if factors_num>2 or factors_rev>2:
        print('the given number is not a emirp number')
    else:
         print('the given number is a emirp number')
emirp_number(int(input('enter the number'))
