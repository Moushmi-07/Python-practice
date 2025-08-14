import pickle as p
def playerdata():
    name=input('enter your name')
    f=open('scoreboard.dat','rb')
    data=p.load(f)
    for i in data:
        print(data[i])
    
#def scoreboard():
