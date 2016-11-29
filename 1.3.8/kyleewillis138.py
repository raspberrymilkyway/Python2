from __future__ import print_function
import random

def guess_winner(players):
    '''The function guess_winner(players) asks you who you think won the lottery
    from the names inputted in players. It makes you guess until you get it right.
    
    Arguments: 
         winner is a randomly chosen player and a string, the value returned is a
        string and is the player who won the lottery
         player is a list of people (probably strings, but they could be ints), 
        there isn't particularly a value returned for this, but it's used in 
        winner...
         guesses is the total number of guesses you've had for this round and an
        int, the value returned is an int and is the total number of guesses
        you have
    '''
    winner = random.choice(players) 

    ####
    # Asks you for your guess as to which player won, prints names of players
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players:
        print(p+', ', end='')

    ####
    ''' Initializes guess variable, and while your input isn't equal to whoever 
    the winner is, it adds 1 to guess. If you guess the correct person, it prints
    a you won statement and returns your guesses' value.
    '''
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

def goguess():
    correct = random.choice(range(1,20))
    guesses = 1
    print('I have a number between 1 and 20 inclusive.')
    while raw_input() != correct:
        haha = raw_input()
        if haha > correct:
            print(haha + ' is too high.')
            guesses += 1
        elif haha < correct:
            print(haha + ' is too low.')
            guesses += 1
    print('Right! My number is ', correct, '! You guessed in ', guesses, 'guesses!')
    return guesses