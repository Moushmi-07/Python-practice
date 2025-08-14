def number(num):
    if num%3==0 and num%7==0:
        print('the number is divisible by both 3 and 7')
    elif num%3==0:
        print('the given number is divisible by 3')
    elif num%7==0:
        print('the given number is divisible by 7')
number(int(input('enter the number')))        
            
        
