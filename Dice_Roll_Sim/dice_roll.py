import sys
import random
import time

def __init__():
  roll()

prev_rolls = []

def roll():
  # ans = how many sides dice has (i.e. 20)
  ans = int(input('How many sides does your dice have? (i.e. 6): '))
  # Generates random numbers between 1 and ans*
  land = random.randint(1, ans)
  
  rolling_ani()
  print(land)
  re_roll()

def re_roll():
  # User response
  res = input('Roll again? (Y/N): ')
  if res == 'Y':
    roll()

def rolling_ani():
  print('Rolling.')
  time.sleep(0.5)
  print('Rolling..')
  time.sleep(0.5)
  print('Rolling...')
  time.sleep(0.5)
  print('Rolling....')

  print('You rolled:')

__init__()
  
