import random

try:
    min = int(input("Min: "))
    max = int(input("Max: "))
    generated = int(input("Amount of numbers to generate: "))

    for i in range(generated):
      print(random.randint(min, max))
      
except ValueError as e:
    print("Enter a number or I'll shoot you. ")
