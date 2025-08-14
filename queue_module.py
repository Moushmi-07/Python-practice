a=[]
def menu():
    print('1.insert')
    print('2.delete')
    print('3.display')
    print('4.exit')
def insert():
    num=input('enter new number')
    a.append(num)
def delete():
    if a==[]:
        print('queue empty')
    else:
        print('delete element is:',a[0])
        del a[0]
def display():
    l=len(a)
    for i in range(0,l):
        print(a[i])
def exit():
    print('thank you')
    
