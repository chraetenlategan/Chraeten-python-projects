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

#Headings
heading = "Welcome to Chraeten guesing game"
heart = ' ❤ '
lives = 3
print(heading.upper())
print(f'You have {heart*lives} lives left')
#get a random number
import random
random_number = random.randint(1,10)
#Initialize
iguessed = False


#Loop until game is finised
while iguessed == False and lives > 0 : 
    user_input = int(input('Please select a random number'))
    if user_input == random_number :
        print(f'Well done you have won in with {heart*lives} lives left')
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
 




