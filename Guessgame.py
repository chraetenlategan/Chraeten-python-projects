# art
death_art = """
      _______
   .-'       `-.
  /             \\
 |   X     X     |
 |       ^       |
 |     '---'     |
  \             /
   '-._______.-'

      YOU DIED
"""

celebration_art = """
  __     ______  _    _  __          _______ _   _ 
  \ \   / / __ \| |  | | \ \        / /_   _| \ | |
   \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
    \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
     | | | |__| | |__| |    \  /\  /   _| |_| |\  |
     |_|  \____/ \____/      \/  \/   |_____|_| \_|
                                                  
            CONGRATULATIONS! YOU WON! 🎉
"""


#Headings
heading = "Welcome to Chraeten's guesing game"
heart = ' ❤ '
lives = 3
print(heading.upper())
print('Guess a number between 1 and 10')
print(f'You have {heart*lives} lives left')

#get a random number
import random
random_number = random.randint(1,10)

#Initialize
iguessed = False
icount = 0


#Loop until game is finised
while iguessed == False and lives > 0 :
    icount += 1 
    user_input = int(input(f'Attemps {icount}: '))
    if user_input == random_number :
        print(f'Well done you have won in with {heart*lives} lives left')
        print(celebration_art)
        iguessed = True
    elif user_input > random_number :
        print(f'The number is smaller than {user_input}')   
        lives -=1
        print(f'You have {heart*lives} left')
    elif user_input < random_number :
        print(f'The number is bigger than {user_input}')
        lives -=1
        print(f'You have {heart*lives} left')
    if lives == 0:
        print(death_art)
 




