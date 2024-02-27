# encryption problem 3
# name: Habeba Mohamed Adly Ahmed 
# ID: 20230118
# ========================== the value for (π) ========================
# Explanation of the code:
# This script calculates an approximation of the value of π using the Leibniz formula. 
# The formula involves iterating through a series of fractions, alternating between addition and subtraction, 
# each involving odd integers. 
# As the number of terms increases, the approximation approaches the value of π/4. 
# The final approximation is obtained by multiplying the sum by 4.

print('the formula for finding the approximate value of π using the relationship established by German mathematician Leibniz (1646–1716). The formula involves starting with 1, subtracting one-third, adding one-fifth, and so on, for each of the odd integers. This process yields a number that approaches the value of π/4 as iterations progress. Therefore, multiplying this value by 4 yields π.')

odd_list = []

while True:
    # Prompt the user to start or end the game
    operation = input('Starting the game enter (1), ending the game enter (0): ')

    # Check if the input is valid
    if operation not in ['0', '1']:
        print('Invalid input. Please enter either 0 or 1.')
        continue
    elif operation == '0':
        # End the game if the user enters '0'
        print('======================== Game Over ==========================')
        break
    else:
        # Inform the user that the game has started
        print('The game started.')

    while True:
        number = input('Enter the number of terms: ')
        try:
            number = int(number)
            break
        except ValueError:
            print('Please enter an integer number')
            continue

    approximation = 0
    odd_integer = 1  # Initialize the odd integer

    # Iterate through the specified number of terms
    for i in range(int(number)):
        if i % 2 == 0:
            approximation += 1 / odd_integer
        else:
            approximation -= 1 / odd_integer
        odd_integer += 2  # Increment the odd integer for the next term

    # Multiply the sum by 4 to obtain the approximation of π
    pi_approximation = approximation * 4

    print("Approximation of π:", pi_approximation)
