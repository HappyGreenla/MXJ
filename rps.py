import random
# Parameters: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):
    if move == 'rock'or move=='paper' or move=='scissors':
        return True;
    else:
        return False;


# Test the check_move function
#print check_move('rock') # Expects: True
#print check_move('paper') # Expects: True
#print check_move('scissors') # Expects: True
#print check_move('roc') # Expects: False
#print check_move(1) # Expects: False

def get_player_move():
    move = raw_input('Pick your move: rock,paper,or scissors?')
    while check_move(move) ==False:
        print('Invalid move;pick again.')
        move = get_player_move()
    return move

#print 'You picked:'+ get_player_move()

def get_computer_move():
    moves =['rock','paper','scissors'];
    return random.choice(moves)
#print get_computer_move()
#print get_computer_move()
#print get_computer_move()

def judge(moveA,moveB):
    if moveA =='rock':
        if moveB =='paper':
            return False
        else:
            return True
    if moveA=='paper':
        if moveB =='rock':
            return True
        else:
            return False
    if moveA=='scissors':
        if moveB== 'paper':
            return True
        else:
            return False

#print judge('rock','paper') # Expected: False
#print judge('rock','scissors') # Expected: True
#print judge('paper','rock') # Expected: True
#print judge('paper','scissors') # Expected: False
#print judge('scissors','rock') # Expected: False
#print judge('scissors','paper') # Expected: True

def play():
    print('Welcome to Welcome to Rock, Paper, Scissors!')
    
    A=get_player_move()
    B=get_computer_move()
  
    print('The computer picked: ' + B)
    
    if A ==B:
        print('Tie.')
    elif judge(A,B):
        print('The winner is you.')
    else:
        print'The winner is computer.'
    
    # Prompt to play again
    play_again = raw_input('Play again? Type `y` or `n`: ')
    
    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')

# Run the game
play()
