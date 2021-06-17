import math
from datetime import datetime
user_choice = 'yes'
def main():
    print()
    width = float(input('Enter the width of the tire in mm (ex 205): '))
    ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
    diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

    volume_output = math.pi * (width**2) * ratio * (width * ratio + 2540 * diameter) / 10000000

    print(f'\nThe approximate volume is {volume_output:.1f} cubic cm.')

    customer_info = input('\nWould you like to buy tires with the dimensions specified?(Yes/No) ')
    while customer_info.lower() != 'no' and customer_info.lower() != 'yes':
        print('\nTry again.')
        customer_info = input('\nWould you like to buy tires with the dimensions specified?(Yes/No) ')

    if customer_info.lower() == 'yes':
        customer_phone_number = input('What is your phone number? ')
        current_date_and_time = datetime.now()
        with open("volumes.txt", "at") as volumes_file:
            print(f'{current_date_and_time.year}-{current_date_and_time.month}-{current_date_and_time.day}, {width}, {ratio}, {diameter}, {volume_output:.1f} - {customer_phone_number}', file=volumes_file)

    else:
        current_date_and_time = datetime.now()
        with open("volumes.txt", "at") as volumes_file:
            print(f'{current_date_and_time.year}-{current_date_and_time.month}-{current_date_and_time.day}, {width}, {ratio}, {diameter}, {volume_output:.1f}', file=volumes_file)



while user_choice.lower() == 'yes':
    main()
    user_choice = input('\nWould you like to run the program again?(Yes/No) ')
    while user_choice.lower() != 'yes' and user_choice.lower() != 'no':
        print('\nTry again.')
        user_choice = input('\nWould you like to run the program again?(Yes/No) ')

print('\nOk, goodbye.')
closing_prompt = input()

