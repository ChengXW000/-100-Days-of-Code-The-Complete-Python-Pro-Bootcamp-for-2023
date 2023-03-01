# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# 0
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#1
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#2
#Write your code below this line 👇

player_choice = input("Let's play game of rock paper scissors. What will you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")

random_num = random.randint(0,2)

if (player_choice == "0"):
  print("\n" + rock)
  print("\nComputer chose: \n")
  if (random_num == 0):
    print(rock)
    print("\nIs a draw")
  elif (random_num == 1):
    print(paper)
    print("\nYou lose")
  else:
    print(scissors)
    print("\nYou win")
elif (player_choice == "1"):
  print("\n" + paper)
  print("\nComputer chose: \n")
  if (random_num == 0):
    print(rock)
    print("\nYou win")
  elif (random_num == 1):
    print(paper)
    print("\nIts a draw")
  else:
    print(scissors)
    print("\nYou lose")
else:
  print("\n" + scissors)
  print("\nComputer chose: \n")
  if (random_num == 0):
    print(rock)
    print("\nYou lose")
  elif (random_num == 1):
    print(paper)
    print("\nYou win")
  else:
    print(scissors)
    print("\nIts a draw")