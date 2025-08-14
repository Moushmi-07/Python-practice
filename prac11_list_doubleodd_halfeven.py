def list1(l):
    for i in range(len(l)):
        if l[i]%2==0:
            l[i]//=2
        else:
            l[i]*=2
x=eval(input('enter a list'))
list1(x)
print('The modified list is',x)
