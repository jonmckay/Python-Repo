"""
This program is Rock,Paper,Scissors. It will have the computer randomly select either Rock, Paper, or Scissors. It will then compare the user's choice and the computer's choice and determine who won.
"""
from random import randint
from time import sleep

options = ['R', 'P', 'S']

loss = "You lost!"
win = "You Won!"

def decide_winner(user_choice, computer_choice):
  print "User chose: %s" % (user_choice)
  print "Computer selecting..."
  sleep(1)
  print "Computer chose: %s" % (computer_choice)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print 'Tie Game!'
  elif user_choice_index == 0 and computer_choice_index == 2:
    print win
  elif user_choice_index == 1 and computer_choice_index == 0:
    print win
  elif user_choice_index == 2 and computer_choice_index == 1:
    print win
  elif user_choice_index > 2:
    print 'Invalid option was selected'
    return
  else:
    print loss
    
def play_RPS():
  print "Welcome to Rock, Paper, Scissors!"
  user_choice = raw_input('Select R for Rock, P for Paper, or S for Scissors: ')
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, len(options)-1)]
  decide_winner(user_choice, computer_choice)

play_RPS()