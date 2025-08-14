def str(s,n,t):
    print('The substring is:','"',t[s-1:s+n-1],'"')
    

t=input('enter the text')
s=int(input('enter the starting position of the substring'))
n=int(input('enter the no.of characters to be read from the given starting point'))
str(s,n,t)
