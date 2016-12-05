import random
def get_guess():
    guess = raw_input('enter your guess:')
    valid = False

    while valid != True:
        try:
            guess = int(guess)
        except Exception:
            print('Invalid input;please enter a whole number.')
            guess = get_guess()
        valid = True

    return guess
#print get_guess()

def compare(numA,numB):
    if numA>numB:
        result= 'high';
    if numA<numB:
        result= 'low'
    return result
#print compare(100,1)  # Expected: 'high'
#print compare(1,100)  # Expected: 'low'
#print compare(99,100) # Expected: 'low'

def play():
    secret_number = random.randint(1,100)
    #    print 'Temporary debugging helper -> The secret number is:' +str(secret_number)
    print "\nI'm thinking of a number between 1 and 100;what do you think it is?"

    user_guess = get_guess()
    count = 1
    #    cmp  =compare(user_guess,secret_number)
    while user_guess != secret_number:
        print 'To '+compare(user_guess,secret_number)+' .Guess again.'
        user_guess = get_guess()
        count = count +1

    print('You got it! The number was '+ str(secret_number))
    print 'It took you '+ str(count)+' guesses.'

play()
