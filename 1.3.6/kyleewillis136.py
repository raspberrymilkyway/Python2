import random
import string

def roll_two_dice():
    print(random.randint(2,12))
    
def guess_letter():
    print(random.choice(string.lowercase))