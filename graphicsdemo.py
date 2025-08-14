from tkinter import *
def run():
    text=Label(text='wrong')
    text.pack()
def run2():
    text=Label(text='correct')
    text.pack()    
screen=Tk()
screen.title('game')
text=Label(text='hello')
text.pack()
name=Entry(text='name')
name.pack()
if name==:
    print(good)
i=0
a=10
for i in range(3):
    click=Button(text='helo',fg='blue',bg='pink',command=run)
    click.place(x=20,y=a)
    click2=Button(text='hello',fg='black',bg='white',command=run2)
    click2.place(x=80,y=a)
    a+=70

