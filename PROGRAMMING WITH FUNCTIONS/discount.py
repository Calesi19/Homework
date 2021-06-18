from datetime import datetime
import math

repeat = 'no'


def main():
    discount = 0
    current = datetime.now()
    weekday = current.isoweekday()

    subtotal = float(input('\nWhat is your subtotal? '))

    if subtotal < 50:
        if weekday == 3 or weekday == 2:
            difference = 50 - subtotal
            print(f'\nTake advantage of our 10% discount today by adding ${difference:.2f} to your cart.')
            user_choice = input('Would you like to add some more items to your cart?(Yes/No) ')

            while user_choice != 'yes' and user_choice != 'no':
                print('\nSorry, try again.')
                user_choice = input('Would you like to add some more items to your cart?(Yes/No) ')

            if user_choice.lower() == 'yes':
                subtotal = float(input('\nWhat is your new subtotal? '))

    if subtotal >= 50:
        if weekday == 3 or weekday == 2:
            discount = subtotal * .1
        

    new_subtotal = subtotal - discount
    sales_tax = new_subtotal * .06
    total = new_subtotal + sales_tax

    if subtotal >= 50:
        print(f'\nDiscount amount: ${discount:.2f}')

    print(f'\nSales tax amount: ${sales_tax:.2f}')
    print(f'Total: ${total:.2f}')


while repeat.lower() == 'no':
    main()
    repeat = input('\nWould you like to run the program again?(Yes/No) ')

print('Ok, goodbye.')
closing_prompt = input('')

print('hello')
print('hello')




