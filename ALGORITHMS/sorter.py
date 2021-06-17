#1. Name:
#      Carlos Lespin
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program is meant to ask the user to input a filename, and then open and sort all the elements inside that specified file.
# 4. What was the hardest part? Be as specific as possible.
#      There wasn't anything specificly hard about coding the program. This is not the algorithm asked for in the instructions
#       from last week, but it accomplishes the same objective. I tried to figure out the other one and couldn't make it work.
# 5. How long did it take for you to complete the assignment?
#      It took me 1 hour and 45 minutes to complete this program.


import json
import os.path

def sort_array(array):
    for descending_value in range(len(array)-1, 0, -1):
        for index in range(descending_value):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
            
    return array

def main():
    file_name = input('\nWhat is the name of the file? ')
    #Checks if file exists
    assert(type(file_name) == str), '\nFile name cannot be a float or integer value.'
    if os.path.isfile(file_name):

        with open(f'{file_name}', 'r') as user_file:
                
            #Saves content in json file as a list (array)
            list = json.load(user_file)
            array = list['array']
            assert(type(array) == list), '\nArray must be a list.'
            #Check list has contents
            if not array:
                print(f'\nThe file {file_name} contains no elements.')
            else:
                for i in sort_array(array):
                    print(i)
    else:
            print('\nFile was not found.')

repeating_prompt = ''   
while repeating_prompt.lower() != 'q':
    main()
    repeating_prompt = input("\nPress 'q' to quit. ")
    