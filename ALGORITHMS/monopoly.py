
#1. Name: 
#      Carlos Lespin
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -This program is meant to gather information and calculate how if its possible
#       for the player to build a hotel on the Pennsylvania Ave. tile in a game of Monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      -The assignment wasn't too hard, but the most challenging part about the was making 
#       sure all loose ends were taking care of.
# 5. How long did it take for you to complete the assignment?
#      -This assigment took about 2.5 hours. to make.



color_prompt = input('\nDo you own all the green properties?(Yes/No) ')


if color_prompt.lower() == 'yes':
    pc_prompt = int(input('\nWhat is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    nc_prompt = int(input('What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    pa_prompt = int(input('What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) '))
    if pa_prompt == 5:
        print('\nYou cannot purchase a hotel if the property already has one.')

    #Calculate houses needed.
    else:
        if pc_prompt > 4:
            pc_houses_needed = 0
        else:
            pc_houses_needed = 4 - pc_prompt

        if nc_prompt > 4:
            nc_houses_needed = 0
        else:
            nc_houses_needed = 4 - nc_prompt

        if pa_prompt > 4:
            pa_houses_needed = 0
        else:
            pa_houses_needed = 4 - pa_prompt

        total_houses_needed = pc_houses_needed + nc_houses_needed + pa_houses_needed

        if total_houses_needed == 0 and pc_prompt == 5:
            print(f"\nSwap Pacific's hotel with Pennsylvania's 4 houses.")
        elif total_houses_needed == 0 and nc_prompt == 5:
            print(f"\nSwap North Carolina's hotel with Pennsylvania's 4 houses.")
        else:

            #Gather information on house and hotel availabilty and user cash.

            houses_available = int(input('\nHow many houses are there to purchase? '))

            if total_houses_needed <= houses_available:
                hotels_available = int(input('How many hotels are there to purchase? '))

                if hotels_available >= 1:
                    total_cost_buildings = 200 * (total_houses_needed + 1)
                    
                    user_cash = int(input('\nHow much cash do you have to spend? '))
                    
                    #Print out result options.
                    


                    if user_cash >= total_cost_buildings:

                        if nc_houses_needed == 0 and pc_houses_needed == 0 and pa_houses_needed == 0:
                            print(f'\nThis will cost ${total_cost_buildings}.\nPurchase 1 hotel and {total_houses_needed} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\n')
                        else:
                            
                            if nc_houses_needed == 0:
                                print(f'\nThis will cost ${total_cost_buildings}.\nPurchase 1 hotel and {total_houses_needed} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {pc_houses_needed} house(s) on Pacific.\n')
                            else:
                                if pc_houses_needed == 0:
                                    print(f'\nThis will cost ${total_houses_needed}.\nPurchase 1 hotel and {total_houses_needed} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {nc_houses_needed} house(s) on North Carolina.\n')
                                else:
                                    print(f'\nThis will cost ${total_cost_buildings}.\nPurchase 1 hotel and {total_houses_needed} house(s).\nPut 1 hotel on Pennsylvania and return any houses to the bank.\nPut {nc_houses_needed} house(s) on North Carolina.\nPut {pc_houses_needed} house(s) on Pacific.\n')

                    else:
                        print('You do not have sufficient funds to purchase a hotel at this time.\n')

                else:
                    print('\nThere are not enough hotels available for purchase at this time.\n')

            else:
                print('\nThere are not enough houses available for purchase at this time.\n ')
            
elif color_prompt.lower() == 'no':
    print('\nYou cannot purchase a hotel until you own all the properties of a given color group.\n')


