import pickle
import random
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words

def rules():
    print('\nRULES:')
    print('-> ENTER "0" WHEN EVER YOU WANT TO QUITE THE GAME.\n-> IF YOU WANT A CLUE U MAY ENTER "1".\n-> ONLY 3 CLUES ARE AVAILABLE FOR A WORD\n-> USE OF EACH CLUE REDUCES YOUR SCORE BY 1. /n->GUESS THE RIGHT WORD WITHIN 6 TRIES.EVERY WRONG ANSWER YOU ENTER YOU LOSE A TRY')
    

def msg():
    global correct
    global wrong
    correct=['\ngreat!,go ahead','\nWOW!,THAT WAS A FABULOUS GUESS','\nGOOD!,KEEP GOING!','\nSUPERB!,YOU ARE ALMOST THERE']
    wrong=['\nsorry!,try something else','\noops!,that was a wrong entry','\nbad luck!','\njust miss!,better luck next time']

def wordmeaning(w):
    x=wordnet.synsets(w)
    global wordm
    wordm=x[0].definition()
    return wordm

def getword():
    global word
    lvl=input('EASY LEVEL-1\nHARD LEVEL-2\nCHOOSE YOUR LEVEL:')
    word_list = words.words()
    if lvl=='1':
        while True:
            word=random.choice(word_list)
            if len(word)>=4 and len(word)<=5:
                try:
                    wordmeaning(word)
                    break
                except IndexError:
                    continue
            else:
                continue
    elif lvl=='2':
        while True:
            word=random.choice(word_list)
            if len(word)>5:
                try:
                    wordmeaning(word)
                    break
                except IndexError:
                    continue
            else:
                continue
    else:
        exit
        


def guess_the_word():
    global fscore
    ch2='1'
    while ch2=='1':
        rules()
        getword()
        score=5
        tries=6
        print('\nMEANING OF THE WORD: ',wordm)
        clue=0
        listword=['_']*(len(word))
        while tries>0:
            if word.upper()==''.join(listword):
                print(listword)
                print('\nCONGRATULATIONS..YOU HAVE FOUND THE WORD:',word.upper(),'(',wordm,')')
                fscore+=score
                print('\n YOUR SCORE IS ',score,'FOR THIS WORD.')
                print('\n YOUR TOTAL SCORE NOW IS',fscore)
                break
            print('\n',listword,'\n')
            letter=input('\nGUESS THE LETTER')
            if letter.upper() in listword:
                print('letter already present,try something else')
                continue
            if letter.isalpha()==True:
                v=False
                
                for index in range(len(word)):
                    if letter.lower()==word[index].lower():
                        listword[index]=letter.upper()
                        v=True
                
                if word.upper()==''.join(listword):
                    print(listword)
                    print('\nCONGRATULATIONS..YOU HAVE FOUND THE WORD:',word.upper(),'(',wordm,')')
                    fscore+=score
                    print('\n YOUR SCORE IS ',score,'FOR THIS WORD.')
                    print('\n YOUR TOTAL SCORE NOW IS',fscore)
                    break
                if v==False:
                    msg()
                    print(random.choice(wrong).upper())
                    tries-=1
                if v==True:
                    msg()
                    print(random.choice(correct).upper())
            if letter=='0':
                confirm=input('\nIF U QUITE U WILL LOSE THE GAME.DO YOU STILL WANT TO QUITE? 1-YES,0-NO')
                if confirm=='1':
                    print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper(),'(',wordm,')')
                    print('\nYOUR SCORE FOR THIS WORD IS 0')
                    print('\nYOUR TOTAL SCORE NOW IS ',fscore)
                    break
                else:
                    continue
            if letter=='1':
                while clue<3:
                    for l in range(len(listword)):
                        if listword[l]=='_':
                            letter=word[l].upper()
                            for index in range(len(word)):
                                if letter.lower()==word[index].lower():
                                    listword[index]=letter.upper()
                                    
                            break
                    
                    clue+=1
                    score-=1
                    break
                
                else:
                    print('\n you have used all the clues'.upper())
                continue
            
            
            
        else:
            print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper(),'(',wordm,')')
            print('\nYOUR SCORE FOR THIS WORD IS 0')
            print('\nYOUR TOTAL SCORE NOW IS ',fscore)
        ch2=input('\nplay again? 1-yes,0-no'.upper())

def jumbled_words():
    global fscore
    ch2='1'
    
    while ch2=='1':
        score=5
        tries=6
        rules()
        getword()
        print('\nMEANING OF THE WORD: ',wordm)
        jumble=random.sample(word.upper(),len(word))
        print('\n',jumble,'\n')
        clue=0
        while tries>0:
            user_word=input('\nGUESS THE WORD: ')
            if user_word.upper()==word.upper():
                print('\nCONGRATULATIONS..YOU HAVE FOUND THE WORD:',word.upper(),'(',wordm,')')
                fscore+=score
                print('\n YOUR SCORE IS ',score,'FOR THIS WORD.')
                print('\n YOUR TOTAL SCORE NOW IS',fscore)
                break
            elif user_word=='0':
                confirm=input('\nIF U QUITE U WILL LOSE THE GAME.DO YOU STILL WANT TO QUITE? 1-YES,0-NO')
                if confirm=='1':
                    print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper(),'(',wordm,')')
                    print('\nYOUR SCORE FOR THIS WORD IS 0')
                    print('\nYOUR TOTAL SCORE NOW IS ',fscore)
                    break
                else:
                    continue
            elif user_word=='1':
                while clue<3:
                    print('\nLETTER',clue+1,'IS: ',word[clue].upper())
                    clue+=1
                    score-=1
                    break
                else:
                    print('\n you have used all the clues'.upper())
                
            else:
                msg()
                print(random.choice(wrong).upper())
                tries-=1
        else:
            print('\nYOU LOST THE GAME. THE WORD WAS:',word.upper(),'(',wordm,')')
            print('\nYOUR SCORE FOR THIS WORD IS 0')
            print('\nYOUR TOTAL SCORE NOW IS ',fscore)
        ch2=input('DO YOU WANT TO CONTINUE? YES-1,NO-2')
            


def npreplayed():
    global pname
    f=open('scoreboard.dat','ab+')
    
    d={'name':pname,'hscore':0}
    print('\nhello',pname.upper(),'FIND MORE NUMBER OF WORDS TO GET MORE POINTS AND BEAT THE SCORE OF YOUR FRIENDS')
    pickle.dump(d,f)
    f.close()
def preplayed():
    global pname
    try:
        f=open('scoreboard.dat','rb')
    except FileNotFoundError:
            npreplayed()
            return 

    while True:
        try:
            data=pickle.load(f)
            if pname.upper()==data['name'].upper():
                print('\nWELCOME BACK',pname.upper(),'YOUR HIGHEST SCORE WAS,',data['hscore'])
                f.close()
                break
            
                
        except EOFError:
            npreplayed()
            break
def sboard():
        f=open('scoreboard.dat','rb')
        print('{:^25}{:^50}'.format('NAME','HIGHEST SCORE'))
        sb=[]
        while True:
            try:
                data=pickle.load(f)
                sb.append(data)
            except EOFError:
                break
        sortsb = sorted(sb, key=lambda d: d['hscore'],reverse=True)
        for i in sortsb:
            print('{:^25}{:^50}'.format(i['name'],i['hscore']))
            
global fscore
fscore=0
global pname
pname=input('ENTER PLAYER NAME')
preplayed()
while True:
    print('\n ENTER THE NUMBER/LETTER GIVEN AGAINST EACH CHOICE FOR GIVING RESPONSE\n')
    print('''\nMENU:
    GUESS THE LETTERS-1\n
    JUMBLED WORDS-2\n
    SCORE BOARD-3\n
    EXIT-0''')
    game=input('\nENTER YOUR CHOICE: ')
    if game=='1':
        print('''\nGUESS THE LETTERS:
              HOW IT WORKS- KEEP GUESSING LETTERS OF THE WORD U THINK IS CORRECT.
              YOU MAY REFER THE MEANING TO GUESS THE WORD.''')
        guess_the_word()
    elif game=='2':
        print('''JUMBLED WORDS:
              HOW IT WORKS-GUESS THE CORRECT WORD WITHIN 6 TRIES WITH THE HELP OF THE JUMBLED LETTERS AND THE MEANING''')
        jumbled_words()
    elif game=='3':
        sboard()
        
    elif game=='0':
        f=open("scoreboard.dat",'rb')

        updata=[]

        while True:
            try:
                udata=pickle.load(f)
                if udata['name']==pname:
                    if udata['hscore']<fscore:
                        udata['hscore']=fscore
                updata.append(udata)    
                
            except EOFError:
                break

        f.close()
        f=open("scoreboard.dat",'wb')
        for i in updata:
            pickle.dump(i,f)
   

        f.close()
        print('\ngame ended'.upper())
        break


