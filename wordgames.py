import random
import pickle as p
global name


def player():
    f=open('scoreboard.dat','ab+')
    playerdata={}
    playerdata[name]=score
    p.dump(playerdata,f)
def rules():
    print('RULES:')
    print('ONCE THE GAME STARTS YOU CAN ENTER "0" WHEN EVER YOU WANT TO QUITE THE GAME.\nIF YOU WANT A CLUE U MAY ENTER "1".\nONLY 3 CLUES ARE AVAILABLE FOR A WORD\n')
    
def msg():
    global correct
    global wrong
    correct=['\ngreat!,go ahead','\nWOW!,THAT WAS A FABULOUS GUESS','\nGOOD!,KEEP GOING!','\nSUPERB!,YOU ARE ALMOST THERE']
    wrong=['\nsorry!,try something else','\noops!,that was a wrong entry','\nbad luck!','\njust miss!,better luck next time']
def wordmeaning(w):
    import nltk
    from nltk.corpus import wordnet
    x=wordnet.synsets(w)
    global wordm
    wordm=x[0].definition()
    return wordm
def word():
    from nltk.corpus import words
    word_list = words.words()
    while True:
        global word
        word=random.choice(word_list)
        try:
            wordmeaning(word)
            break
        except IndexError:
            continue
    print(wordm)
##def category():
##    print('''
##fruits and vegetables-1
##colours-2
##accessories-3
##foods-4\n'''.upper())
##    menu=int(input('CHOOSE THE CATEGORY YOU WANT TO PLAY: '))
##    if menu==1:
##        fname='fruits.dat'
##    elif menu==2:
##        fname='colours.dat'
##    elif menu==3:
##        fname='accessories.dat'
##    elif menu==4:
##        fname='foods.dat'
##        
##    with open(fname,'rb') as f:
##        global words
##        words=p.load(f)
        
        
def guess_the_word():
    global score
    score=0
    tries=6
    #category()
    rules()
    word()
    clue=0
    ch2='1'
    while ch2=='1':
        #word=random.choice(words)
        listword=['_']*(len(word))
        while tries>0:
            print('\n',listword,'\n')
            letter=input('\nGUESS THE LETTER')
            if letter=='0':
                confirm=input('\nIF U QUITE U WILL LOSE THE GAME.DO YOU STILL WANT TO QUITE? 1-YES,0-NO')
                if confirm=='1':
                    print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper())
                else:
                    continue
            if letter=='1':
                while clue<3:
                    for l in range(len(listword)):
                        if listword[l]=='_':
                            listword[l]=word[l].upper()
                            break
                    
                    clue+=1
                    break
                
                else:
                    print('\n you have used all the clues'.upper())
            else:
                v=False
                for y in range(len(word)):
                    if letter.lower()==word[y].lower():
                        listword[y]=letter.upper()
                        v=True
                if word.upper()==''.join(listword):
                    print('\nCONGRATULATIONS..YOU HAVE FOUND THE WORD:',word.upper())
                    for c in range(0,3):
                        if clue==c:
                            score+=5-c
                    player()
                    print(score)
                        
                    #s.syn(word)
                    break
            
                if v==False:
                    msg()
                    print(random.choice(wrong).upper())
                    tries-=1
                if v==True:
                    msg()
                    print(random.choice(correct).upper())
        else:
            print('sorry your tries are over')
            print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper())
            
            break
        ch2=input('\nplay again? 1-yes,0-no'.upper())
def jumbled_words():
    #category()
    tries=6
    rules()
    word()
    #global word
    #word=random.choice(words)
    jumble=random.sample(word.upper(),len(word))
    jumbled_word=''.join(jumble)
    print('\n',jumbled_word,'\n')
    clue=0
    while tries>0:
        user_word=input('\nGUESS THE WORD: ')
        if user_word.upper()==word.upper():
            print('\nCONGRATULATIONS..YOU HAVE FOUND THE WORD:',word.upper())
            break
        elif user_word=='0':
            confirm=input('\nIF U QUITE U WILL LOSE THE GAME.DO YOU STILL WANT TO QUITE? 1-YES,0-NO')
            if confirm=='1':
                print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper())
                break
            else:
                continue
        elif user_word=='1':
            while clue<3:
                print('\nLETTER',clue+1,'IS: ',word[clue].upper())
                clue+=1
                break
            else:
                print('\n you have used all the clues'.upper())
                
        else:
            msg()
            print(random.choice(wrong).upper())
            tries-=1
    else:
        print('your tries are over!')
        print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper())
    

name=input('enter player name')

while True:
    print('''
GUESS THE WORD-1\n
JUMBLED WORDS-2\n
NEW PLAYER-3\n
EXIT-0''')
    game=input('\nCHOOSE YOUR GAME: ')
    if game=='1':
        guess_the_word()
    elif game=='2':
        jumbled_words()
    elif game=='0':
        print('\ngame ended'.upper())
        break
    
    
        
            
            


