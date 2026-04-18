#Welcome Message: Greet the user and define the mission using the print() function.
#Input Handling: Use the input() function to prompt the user and .lower() to convert input to lowercase to handle variations in user input (e.g., "Left" vs "left").
#Branching Paths (if/elif/else):
#Decision 1: Ask user to go "left" or "right".
#If "right", print "Fall into a hole. Game over." and end the game.
#If "left", proceed to Decision 2.
#Decision 2: Ask user to "swim" or "wait" at the lake.
#If "swim", print "Attacked by trout. Game over.".
#If "wait", proceed to Decision 3.
#Decision 3: Ask user to choose one of three doors: "red", "yellow", or "blue".
#If "red", print "Burned by fire. Game over.".
#If "blue", print "Eaten by beasts. Game over.".
import random

print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    /      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')

print('Welcome to Treasure Island')
print('Your mission is to find the hidden treasure')
critical_path=input('You are at a cross road, where do you want to go? Type "left" or "right" ').lower()
if critical_path == 'left':
    print('You felt in a crocodile pit, you lose')
else:
    print('Move to the next level')

lake =input( 'You see a lake,near the lake there is a wood boat, type "take the boat" or "stay"     ').lower()
if lake == 'take the boat':
    print('The boat had a hole, you lose')
else:
     print('Move to the next level')

Cave= input(' You see a new boat, you take it and sail  until you reach a cave, on that cave there are 2 paths, Type "go up" or "go down"  ').lower()
if Cave == "go down":
    print('You felt in a hole with fire, you lose')
else:
     print('Move to the next level')

# FINAL CHALLENGE
random_number = random.randint(1, 100)
N_lives = 5

print("Final challenge: guess the number to open the treasure!")

while N_lives > 0:
    guess = int(input('Guess a number: '))

    if guess < random_number:
        print('Too low')
        N_lives -= 1
    elif guess > random_number:
        print('Too high')
        N_lives -= 1
    else:
        print("That's the right number!")
        print("You won Treasure Island!")
        break

    print(f'Lives left: {N_lives}')

if N_lives == 0:
    print(f'You lose! The number was {random_number}')
    print('Game over')
