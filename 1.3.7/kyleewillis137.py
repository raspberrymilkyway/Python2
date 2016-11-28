# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
import random

def days():
    ''' The code prints every day of the week (because of MTWRFSS and for)
    and days from 5 up to, but not including, 8 (because range(5,8))
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below?  
    '''They make lists. The random choice has to have the () on the end.
    The a += [random.choice... line becomes part of a list.
    '''
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    # a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()

def roll_hundred_pair():
    roll = []
    for dice in range(100):
        die = random.randint(1,6)
        dontdie = random.randint(1,6)
        roll += [die + dontdie]
    
    plt.hist(roll, bins = 11)
    plt.show()
    
def dice(n):
    total = 0
    for dice in range(n):
        die = random.randint(1,6)
        total += die
    print('Roll was ' + str(total))
    
def matches(ticket, winners):
    total = 0
    for each in ticket:
        if each in winners:
            total += 1
    print(total)
    
def hangmanDisplay(guessed,secret):
    quiet = ''
    for each in secret:
        if each in guessed:
            quiet += each
        elif each == ' ':
            quiet += ' '
        else:
            quiet += '-'
    print(quiet)
        
def report(guess, secret):
    right = 0
    wrong = 0
    shh = [right, wrong]
    if guess == secret:
        right += len(secret)
        print("Bravo!")
    for guess in secret:
        #is this a thing I can do?
        #I don't have time to finish this, so I'll leave it at this. :(
    print(shh)