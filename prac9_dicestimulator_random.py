#to write a random number generator that generates random numbers between 1 and 6 (that simulates a dice)
import random
def roll():
    dice=random.randint(1,6)
    print(dice)
ch1=input('start the game?y/n')
if ch1=='y':
    print('''RULES:
ENTER- y TO ROLL THE DICE
             -p TO PASS THE DICE TO THE NEXT PLAYER
             -n TO END THE GAME''')
    while True:
        user1=input('\nplayer1:do you want to roll the dice?y/p/n')
        if user1=='y':
            roll()
        elif user1=='n':
            print('\ngame ended')
            break
        elif user1=='p':
            print('\nDICE PASSED TO NEXT PLAYER\n ')
        user2=input('\nplayer2:do you want to roll the dice?y/p/n')
        if user2=='y':
            roll()
        elif user2=='n':
            print('game ended')
            break
        elif user2=='p':
            print('\nDICE PASSED TO NEXT PLAYER\n ')
else:
    print('\ngame ended')
