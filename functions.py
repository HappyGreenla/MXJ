#def multiply(a,b):
#    result = a*b
#    return result

#multiply(4,5)

#print(multiply(-1, -55)) # 55
#print(multiply(3, 'Hello')) # 'HelloHelloHello'

#def isPositive(a):
#    if a>0:
#        return True
#    else:
#        return False

#print(isPositive(4))
#print(isPositive(-9.9))

#import random
#def draw_random_card():
#    cards = [1,2,3,4,5,6,7,8,9,10,10,10,11]
#    random.shuffle(cards)
#   return cards.pop()

#print(draw_random_card())
#print(draw_random_card())
#print(draw_random_card())

def display_winner(winner,msg):
    if winner =='Player':
        outcome = 'You win!'
    else:
        outcome = 'Computer wins!'
    print(outcome +'(' + msg+')')

display_winner('Player','you were closest to 21')
display_winner('Computer', 'It was closest to 21')

def mystery(x, y, z):
    return x+y*z

# ??? Your code here

# Test this function:
print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'

def calculate_tip(meal,tip_amount):
    if tip_amount =='A':
        return int(meal*.20)
    elif tip_amount =='B':
        return meal*.18
    elif tip_amount=='C':
        return meal*.15

print(calculate_tip(30.50, 'C')) # Expected: 4.575
print(calculate_tip(15.00, 'B')) # Expected: 2.7
print(calculate_tip(20.00, 'A')) # Expected: 4
