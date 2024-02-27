# File Name: CS112_A1_T2_1_20230118.py
# Purpose: Implementing the 100 Game where two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Habeba Mohamed Adly Ahmed 
# ID: 20230118
# ======================================= 100 Game ==============================================
# Welcome message for the 100 Game
print('The 100 Game: Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.')

# Initialize the sum value to keep track of the total sum
the_sum_value = 0

# List of valid game values
game_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Infinite loop to handle game plays
while True:    
    # Prompt the user to start or end the game
    operation = input('Starting the game enter (1), ending the game enter (0): ')
    
    # Check if the input is valid
    if operation not in ['0', '1']:
        print('Invalid input. Please enter either 0 or 1.')
        continue
    elif operation == '0':
        # End the game if the user enters '0'
        print ('======================== Game Over ==========================')
        break
    else:
        # Inform the user that the game has started
        print('The game started.')
        
    # Loop for each player's turn
    while True:
        # First player's turn
        while True:
            # Prompt the first player to enter a number from 1 to 10
            player1 = input('The first player enters a number from 1 to 10: ')
            if player1 in game_values:
                the_sum_value += int(player1)  # Add the player's input to the sum value
                break
            else:
                print('Please enter a number from 1 to 10.')
        
        # Check if the sum value is within the game bounds
        if the_sum_value <= 100:
            print('The sum value is:', the_sum_value)
        
        # Check if the first player wins
        if the_sum_value == 100:
            print('The first player won!')
            break
        elif the_sum_value > 100:
            # Inform the first player to enter a smaller value
            print('Please enter a value less than or equal to:', int(player1) - (the_sum_value - 100))
            the_sum_value -= int(player1)  # Adjust the sum value
            print('The sum value is:', the_sum_value)
            continue
        
        # Second player's turn
        while True:
            # Prompt the second player to enter a number from 1 to 10
            player2 = input('The second player enters a number from 1 to 10: ')
            if player2 in game_values:
                the_sum_value += int(player2)  # Add the player's input to the sum value
                break
            else:
                print('Please enter a number from 1 to 10.')
        if the_sum_value <= 100:
            print('The sum value is:', the_sum_value)
        
        # Check if the second player wins
        if the_sum_value == 100:
            print('The second player won!')
            break
        elif the_sum_value > 100:
            # Inform the second player to enter a smaller value
            print('Please enter a value less than or equal to:', int(player2) - (the_sum_value - 100))
            the_sum_value -= int(player2)  # Adjust the sum value
            print('The sum value is:', the_sum_value)
            continue