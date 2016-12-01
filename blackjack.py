import random

#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#print(cards)

random.shuffle(cards)
print(cards)

#Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: '+ str(player_card1))
print('Computer card: '+ str(computer_card1))

print(cards)

decision = raw_input("\nIf you want to stay type 's',if you want to hit type 'h':")

#Round2
#random.shuffle(cards)
if decision =='s':
    player_card2 = 0
elif decision =='h':
    player_card2 = cards.pop()
else:
    print('Wrong input,defalt hit')
    player_card2 = cards.pop()

computer_card2 = cards.pop()

print('Player card:'+ str(player_card1) +' '+str(player_card2))
print('Computer card:'+ str(computer_card1)+' '+str(computer_card2))
print(cards)

#Round3
#random.shuffle(cards)
decision2= raw_input("\nIf you want to stay type 's',if you want to hit type 'h':")
if decision2 =='s':
    player_card3 = 0
elif decision2 =='h':
    player_card3 = cards.pop()
else:
    print('Wrong input,defalt hit')
    player_card3 = cards.pop()

if computer_card1+computer_card2 < 16:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

print('Player card:'+ str(player_card1) +' '+str(player_card2)+' '+str(player_card3))
print('Computer card:'+ str(computer_card1)+' '+str(computer_card2)+' '+str(computer_card3))
print(cards)

player_card = player_card3+player_card2+player_card1
computer_card = computer_card3+computer_card2+computer_card1

if player_card > 21 and computer_card > 21:
    print('Tie.')
elif player_card >21:
    print('The winner is Computer.Player busted.')
elif computer_card > 21:
    print('The winnner is You,Computer busted.')
elif player_card == computer_card:
    print('Tie.')
elif player_card > computer_card:
    print('You won.')
else:
    print('Computer won.')
