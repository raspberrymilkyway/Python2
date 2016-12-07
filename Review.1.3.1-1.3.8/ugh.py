from Variables131138 import nameList
import random

def piglatin(names):
    pigLatinList = []
    for name in nameList:
        if name[0] in 'AEIOU':
            name += 'ay'
            print name
            pigLatinList += name
        else:
            name += name[0] + 'ay'
            print name[1:]
            pigLatinList += name[1:]
    return pigLatinList  
    
def nameGuesser(names):
    beta = nameList
    beta.sort()
    correct = random.choice(names)
    print('Hey, guess a name!')
    print beta
    guess = 42
    while guess != correct:
        guess = raw_input()
        if guess < correct:
            print 'The correct name is further down the list.'
        if guess > correct:
            print 'The correct name is before your guess.'
    print 'Bravo! You guessed right!'