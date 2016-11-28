from __future__ import print_function #did we need this part?

def age_limit_output(age):
    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print(str(age) + ' is below the age limit.')
    else:
        print(str(age) + ' is old enough.')
    print('Minimum age is ' +str(AGE_LIMIT))
    
def report_grade(percent):
    MASTERY = 80
    if percent >= MASTERY:
        print ('A grade of ' + str(percent) + ' percent shows mastery.')
        print ('Keep up the good work!')
    else:
        print ('A grade of ' +str(percent) + ' does not show mastery.')
        print ('Seek extra practice or help.')
        
def letter_in_word(guess, word):
    if len(guess)==1 and guess in word:
        return True
    else:
        return False
        
def hint(color, secret):
    if color in secret:
        print('The color ' + str(color) + ' IS in the secret sequence.')
    else:
        print('The color ' + str(color) + ' IS NOT in the secret sequence.')