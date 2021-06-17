


while game_continues = True:
    if time > 120:
        print('You lose')
        game_continues = False
    else:
        
        if player_fuel == 0:
            print('You lose')
            game_continues = False


        if collision == True:   #Both, hitting a wall and hitting an obstacle, count as collision.
            if player_lives - 1 == 0:
                print('You lose')
                game_continues = False

            elif player_lives >= 2:
                player_lives - 1


        if player_power_up_obtained == True:
            if power_up == time_bonus:
                time - 20
            elif power_up == extra_life:
                player_lives += 1
        

        if player_location_coordinate == level_ending_coordinate:
            print('You won')
            game_continues = False

