import random

# promt the user 
print("Welcome to Rock, Paper, Scissors!")
print("Choose a number: 1=Rock, 2=Paper, 3=Scissors")
user_choice = int(input("Enter your choice (1-3): "))

# Validate input 
if user_choice not in [1, 2, 3]:
    print("Invalid choice. Please choose a number between 1 and 3.")
else: 
    # Generate a random choice for the computer
    computer_choice = random.randint(1, 3)

# Map numbers to choices for display
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

#Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 3 and computer_choice == 2):
    print("You win!")

else:
    print("You lose!")
