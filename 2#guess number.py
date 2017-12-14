import random
import simplegui
import math

num_range=100
x=0
remain=7

def new_game():
    f.start()
    print 'New game, Range is from 0 to',num_range
    print 'Number of remaining guesses is',remain
    print ''
    
def range100():
    global x,remain,num_range
    num_range=100    
    remain=int(math.ceil(math.log(num_range,2)))
    new_game()
    x=random.randrange(0,num_range)
    
def range1000():
    global x,remain,num_range
    num_range=1000
    remain=int(math.ceil(math.log(num_range,2)))
    new_game()
    x=random.randrange(0,num_range)

def get_input(guess):
    global x,remain,num_range
    g=int(guess)
    remain-=1
    if remain<0:
            print 'You lose the game.'
            print ''
            range100()
    elif g==x:
            print 'Guess was',g
            print 'Number of remaining guesses is',remain
            print 'You win.'
            print ''
            range100()
    elif g>x:
            print 'Guess was',g
            print 'Number of remaining guesses is',remain
            print 'Lower'
            print ''
    elif g<x:
            print 'Guess was',g
            print 'Number of remaining guesses is',remain
            print 'Higher'
            print ''
    
    
f=simplegui.create_frame('Quess the number',200,200)
f.add_button('Range is [0,100)',range100,200)
f.add_button('Range is [0,1000)',range1000,200)
f.add_input('Enter a guess',get_input,200)

new_game()

