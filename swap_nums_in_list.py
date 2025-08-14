def swap(num,n):
    n=len(num)
    if n%2==0:
        for i in range(0,n,2):
            j=i+1
            num[i],num[j]=num[j],num[i]
        print(num)
swap(eval(input('enter the list')),0)

