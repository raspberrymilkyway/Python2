from __future__ import print_function # must be first in file 
import random

def food_id(food):
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']    
    starchy = ['banana', 'potato']    # Check the category and report
    if food in fruits:        
        if food in citrus:            
            return 'Citrus, Fruit'        
        else:            
            return 'NOT Citrus, Fruit'    
    else:        
        if food in starchy:            
            return 'Starchy, NOT Fruit'        
        else:            
            return 'NOT Starchy, NOT Fruit'

def food_id_test():
    works = True    
    if food_id('orange') != 'Citrus, Fruit':        
        works = False        
        print('orange bug in food id()')
    if food_id('banana') != 'NOT Citrus, Fruit':        
        works = False        
        print('banana bug in food_id()')     # Add tests so that all lines of code are visited during test
    if food_id('potato') != 'Starchy, NOT Fruit':        
        works = False       
        print('potato bug in food id()')
    if food_id('apple') != 'NOT Citrus, Fruit':        
        works = False        
        print('apple bug in food id()') 
    if works:        
        print('food_id passed all tests')    
        return works
        
def f(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print(str(n) + ' is a multiple of 6')
            else:
                print(str(n) + ' is even')
        else:
            print(str(n) + ' is odd')
    else:
        print(str(n) + ' is not an integer')
        
def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess > secret:
            print('Too high, my number was', secret, end='!\n')
        if guess < secret:
            print('Too low - my number was', secret, end='!\n')
    else:
        print('Right on! I was number', guess, end='!\n')
        
def quiz_decimal(low, high):
    print('Type a number between', low, 'and', high, end=':\n')
    n = float(raw_input(''))
    if n > low and n < high:
        print('Good!', low, '<', n, '<', high, sep=' ')
    elif n > high:
        print('No,', n, 'is greater than', high, sep=' ')
    elif n < low:
        print('No,', n, 'is less than', low, sep=' ')
    else:
        print('No,', n, 'is one of the endpoints of the interval', sep=' ')