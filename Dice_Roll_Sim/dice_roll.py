import sys
import random

def __init__():
  roll()

def roll():
  # Generates random numbers between 1 and 6
  ch = random.randint(1,6)
  print(ch)
  print(side_number())

def side_number():
  ans = int(input('How many sides does your dice have? (i.e. 6): '))
  return ans

__init__()
  
