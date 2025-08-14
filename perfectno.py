def num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=n
        if sum==n:
            return 0
        else:
            return -1
num(6)
