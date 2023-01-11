rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

computer = int(random.randint(0, 2))
print("Do you feel lucky?\nLet's play Rock, Paper, Scissors!")
human = int(input("Type 1 for Rock, 2 for Paper, or 3 for Scissors."))

words = ["rock", "paper", "scissors"]

pictures = [rock, paper, scissors]


if (human - 1) == computer:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You have drawn. Why not try again?")
elif human == 1 and computer == 2:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You won. Congratulations!")
elif human == 2 and computer == 0:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You won. Congratulations!")
elif human == 3 and computer == 1:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You won. Congratulations!")
elif human == 1 and computer == 1:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You lost. Why not try again?")
elif human == 2 and computer == 2:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You lost. Why not try again?")
elif human == 3 and computer == 0:
  print(words[human - 1] + pictures[human - 1] + words[computer] + pictures[computer] + "You lost. Why not try again?")