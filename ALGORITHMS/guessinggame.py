# 1. Name:
#      -Carlos Lespin
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      -The purpose of the program is to have it generate a random number between a range, and then
#       have the user guess numbers until they guess the generated number. The program will hint the user on how high or low their guess is 
#       compared to the generated number.
# 4. What was the hardest part? Be as specific as possible.
#      -There wasn't anything I found hard about the assignment.
# 5. How long did it take for you to complete the assignment?
#      30 Minutes

import random
user_choice = 'yes'
def main():
    user_guesses = []
    tries = 1
    print('''\nThis is the "guess a number" game.
You try to guess a random number in the smallest number of attempts.''')

    ceiling_value = int(input('Pick a positive integer: '))
    generated_value = random.randint(1,ceiling_value)
    print(f'Guess a number between 1 and {ceiling_value}. \n')

    user_guess = int(input('> '))

    while user_guess != generated_value:
        if user_guess > generated_value:
            print('\n   Too high!')
        if user_guess < generated_value:
            print('\n   Too low!')
        tries += 1
        user_guesses.append(user_guess)
        user_guess = int(input('\n> '))

    user_guesses.append(user_guess)
    print(f'''\nYou were able to find the number in {tries} guesses.
The numbers you guessed were: {user_guesses}''')

while user_choice.lower() == 'yes':
    main()
    user_choice = input('Would you like to run the program again?(Yes/No) ')
    while user_choice.lower() != 'no' and user_choice.lower() != 'yes':
        print('\nTry again.')
        user_choice = input('Would you like to run the program again?(Yes/No) ')

print('\nOk, goodbye.')
close_prompt = input('')

