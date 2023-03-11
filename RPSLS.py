import random
import time

# Define the game rules and outcomes
RULES = {
    'rock': {'scissors', 'lizard'},
    'paper': {'rock', 'spock'},
    'scissors': {'paper', 'lizard'},
    'lizard': {'paper', 'spock'},
    'spock': {'rock', 'scissors'}
}

WIN_MSG = {
    'rock_scissors': 'Rock crushes scissors!',
    'rock_lizard': 'Rock crushes lizard!',
    'paper_rock': 'Paper covers rock!',
    'paper_spock': 'Paper disproves Spock!',
    'scissors_paper': 'Scissors cuts paper!',
    'scissors_lizard': 'Scissors decapitates lizard!',
    'lizard_paper': 'Lizard eats paper!',
    'lizard_spock': 'Lizard poisons Spock!',
    'spock_rock': 'Spock vaporizes rock!',
    'spock_scissors': 'Spock smashes scissors!'
}

LOSE_MSG = {
    'scissors_rock': 'Rock crushes scissors! You lose.',
    'lizard_rock': 'Rock crushes lizard! You lose.',
    'rock_paper': 'Paper covers rock! You lose.',
    'spock_paper': 'Paper disproves Spock! You lose.',
    'paper_scissors': 'Scissors cuts paper! You lose.',
    'lizard_scissors': 'Scissors decapitates lizard! You lose.',
    'paper_lizard': 'Lizard eats paper! You lose.',
    'spock_lizard': 'Lizard poisons Spock! You lose.',
    'rock_spock': 'Spock vaporizes rock! You lose.',
    'scissors_spock': 'Spock smashes scissors! You lose.'
}

TIE_MSG = "It's a tie!"

# Define the delay between each character print
PRINT_DELAY = 0.05

# Initialize the score
score = 0

# Print the welcome message with a typing effect
welcome_msg = "Welcome to Rock Paper Scissors Lizard Spock!\n\n"
for char in welcome_msg:
    print(char, end='', flush=True)
    time.sleep(PRINT_DELAY)

# Print the game rules with a typing effect
rules_msg = "The rules are simple:\n\nRock crushes Scissors and Lizard.\nPaper covers Rock and disproves Spock.\nScissors cuts Paper and decapitates Lizard.\nLizard eats Paper and poisons Spock.\nSpock vaporizes Rock and smashes Scissors.\n\n"
for char in rules_msg:
    print(char, end='', flush=True)
    time.sleep(PRINT_DELAY)

# Start the game loop
while True:
    # Ask the user to input their choice
    user_choice = input("\nChoose rock, paper, scissors, lizard, or spock (or quit to exit): ").lower()
    
    # Quit the game if the user enters 'quit'
    if user_choice == 'quit':
        print("\nThanks for playing!")
        break
    
    # Check if the user's choice is valid
    if user_choice not in RULES:
        print("\nInvalid choice. Please try again.")
        continue
    
    # Generate a random choice for the computer
    computer_choice = random.choice(list(RULES.keys()))
    
    # Print the user's choice with a typing effect
    print("\nYour choice: ", end='', flush=True)
    for char in user_choice:
        print(char, end='', flush=True)
        time.sleep(PRINT_DELAY)
        
        # Determine the outcome and print the result with a typing effect
    outcome = user_choice + '_' + computer_choice
    
    if outcome in WIN_MSG:
        print("\n\n" + WIN_MSG[outcome])
        score += 1
    elif outcome in LOSE_MSG:
        print("\n\n" + LOSE_MSG[outcome])
    else:
        print("\n\n" + TIE_MSG)
    
    # Print the score
    print("\nScore: ", score)
