import random

print('WELCOME TO THE ROCK, PAPER, SCISSORS GAME')

print( """
    _______
---'   ____)
      (_____ )
      (_____ )
      (____)
---.__(___)
"""

 """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


middle_finger= """
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(.......... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
"""

rock = """
    _______
---'   ____)
      (_____ )
      (_____ )
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Player = input('Choose "rock", "paper" or "scissors": ').lower()

computer = random.choice(["rock", "paper", "scissors"])

print("\nYour choice:")
if Player == "rock":
    print(rock)
elif Player == "paper":
    print(paper)
elif Player == "scissors":
    print(scissors)

print("\nComputer chose:")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
elif computer == "scissors":
    print(scissors)

# GAME LOGIC
if Player == computer:
    print("It's a draw!")
elif (Player == "rock" and computer == "scissors") or \
     (Player == "paper" and computer == "rock") or \
     (Player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
    print(middle_finger)