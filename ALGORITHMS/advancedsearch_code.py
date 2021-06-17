#1. Name:
#      Carlos Lespin
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program is meant to open a file determined by the user and search a specific word
#      inside that file.        
# 4. Algorithmic Efficiency
#      This is code has an efficiency of  O(log n); because it contains a loop and cuts the size of the list
#      by a fraction through every iteration of the loop.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to make the program determine if the word should be in the second half or first half after
#      dividing the word list in half. Eventually I figured it was as simple as... word (> or <) word_in_list.
# 6. How long did it take for you to complete the assignment?
#      This took about three hours to complete.


import json
import os.path


#Function to conduct search through list. It divides list in half until it narrows it down to one result.
def arraysearch(array, word):
    iterations = 0 #Variable to keep track of how many items in the list have been checked or how many times the loop has repeated itself.
    
    first = 0 
    last = len(array)-1
    index = -1
    while (first <= last) and (index == -1):
        iterations += 1

        #Finds middle of the list and keeps the index number if it matches the user's search
        middle = (first + last) // 2
        if array[middle] == word:
            index = middle
        
        #Determines in which half of the list the word is in and keeps that half
        else:
            if word < array[middle]:
                last = middle -1
            else:
                first = middle + 1


    return index, iterations

def open_file_and_search(file_name, user_search):
    #Open json file
    with open(f'{file_name}', 'r') as user_file:
        
        #Saves content in json file as a list (array)
        list = json.load(user_file)
        array = list['array']

        #Check list has contents
        if not array:
            print(f'\nThe file {file_name} contains no elements.\n')

        else: #Conduct search through list
            index_number, iterations = arraysearch(array, user_search)
        
            #Print results of search
            if array[index_number] == user_search:
                print(f'\nWe found \"{user_search}\" in {file_name}.')
            else:
                print(f"\nSorry, \"{user_search}\" couldn't be found in {file_name}.")
            
            #Print how many iterations it took to find result.
            print(f'It took {iterations} iterations through the list.\n')

def main():
    #Get user input
    file_name = input('\nWhat is the name of the file? ')
    user_search = input('What name are we looking for? ')

    #Checks if file exists
    if os.path.isfile(file_name):
        open_file_and_search(file_name, user_search)
    else:
        print('\nFile was not found.\n')

    
repeat = ' '
while repeat.lower() != 'q':
    main()
    repeat = input("Press 'q' to exit. ")


