def showlarge(str):
    x=str.split('')
    for i in range(len(x)+1):
        if len(x[i])>4:
            print(x[i])
showlarge('hello world')            
