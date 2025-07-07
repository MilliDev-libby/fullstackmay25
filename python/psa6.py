import random

print("Welcome to roll the dice!")
print("Choose a number between 1 and 6")
user_choice = int(input("Enter your choice (1-6): ")) 

# Validate input
if user_choice < 1 or user_choice > 6:
    print("Invalid choice. Please choose a number between 1 and 6.")
else:
    # Generate a random choice for the computer
    computer_choice = random.randint(1,6)
    print(f'You chose: {user_choice}')
    
    tries = 0 
    computer_choice = 0


    # Loop until the computer rolls the user's choice
    while computer_choice != user_choice:
        computer_choice = random.randint(1, 6)
        tries += 1 
        print(f"roll {tries}: {computer_choice}")
    
    print(f"\nYou have successfully rolled {user_choice}!") 
    print(f"It took you {tries} tries.")