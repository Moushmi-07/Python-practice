##write a program to search an element in a list and
##display the frequency of the element present in the list with its location
def create():
    l1=eval(input('ENTER A LIST'))
    print('LIST CREATED')
    global l
    l=l1
def read():
    global l
    print('the list is',l)
def search():
    global l
    #y=int(input("enter 1 to search a number,enter 2 to search a string"))
    global n
    #if y==1:
    n=int(input('enter the element to be searched'))
    #if y==2:
        #n=input('enter the element to be searched')
    i=-1
    value=True
    for x in l :
        i+=1
        if x==n:
            print('the elemnt',n,'is pressent in the list with location',i+1,'and the index',i)
            value=False
    if value==True:
        print('the element does not exist in the list')
def count():
    global l
    global n
    freq=0
    for i in l:
        if i==n:
            freq+=1
    print(n,'has occured',freq,'times in the list')
ch1='y'

while ch1=='y':
    print('''ENTER
          1 FOR CREATING LIST
          2 FOR DISPLAYING LIST
          3 FOR SEARCHING AN ELEMENT IN THE LIST AND DISPLAYING ITS LOCATION
          4 FOR DISPLAYING THE FREQUENCY OF THE ELEMENT
          5 FOR EXIT''')
    print('')
    ch2=int(input('enter a valid choice of number according to above info'))
    if ch2==1:
        create()
    if ch2==2:
        read()
    if ch2==3:
        search()
    if ch2==4:
        count()
    if ch2==5:
        print('THANK YOU')
        break
    print('')
    ch1=input('do you want to continue? y/n')
else:
    print('THANK YOU')
    


