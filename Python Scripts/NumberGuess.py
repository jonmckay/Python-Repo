"""
This program has the user guess a number and rolls the dice. It will decide a winner based on how close the user is to the total value.
"""
from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input('Guess a number: '))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum Value Is: %s" % (str(max_val))
  sleep(1)
  user_guess = get_user_guess()
  
  if user_guess > max_val:
    print "Your guess was too high"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "First roll: %d" % (first_roll)
    sleep(1)
    print "Second roll: %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total roll: %d" % (total_roll)
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "You Won!"
      return
    else:
      print "You Lost"

roll_dice(6)