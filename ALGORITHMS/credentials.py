# 1. Name:
#      Carlos Lespin
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -This program takes the user's input for their username and password. 
#       If both match the information/credentials stored in a Json file, then 
#       it will grant authentication to the user, otherwise, it won't.-
# 4. What was the hardest part? Be as specific as possible.
#      -For a long while, I couldn't figure out why my loops weren't working. I had to try different schematics
#       until I found the way for the loops to make sense and work correctly.
# 5. How long did it take for you to complete the assignment?
#      -Little under 3 hours.-
import json

username_input = input('\nUsername: ')
password_input = input('Password: ')


with open('Lab02.json') as credential_file:
    credentials = json.load(credential_file)
    usernames = credentials['username']
    passwords = credentials['password']
    authorization = False

    for u in usernames:
        if username_input == u:
            index_location = usernames.index(u)
            if password_input == passwords[index_location]:
                authorization = True
            else:
                authorization = False

            break

    if authorization == True:
        print('\nYou are authenticated!')
    if authorization == False:
        print('\nYou are not authorized to use the system.')

    

