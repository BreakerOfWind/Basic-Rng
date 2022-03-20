import random
from random import randrange
import time
from random import *

test = 0
min = 0
max = 10
limit = 10 # Set the limit of numbers generated

while test != limit:
  print(randrange(min,max))
  test = test + 1
  if test >= limit:
    break
