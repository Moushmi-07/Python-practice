lower=int(input('enter the lower limit'))
upper=int(input('enter the upper limit'))
for x in range(lower,upper):
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    if sum==x:
        print(x)
