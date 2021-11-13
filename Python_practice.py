# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
continue_playing = ["y","n"] 
while  continue_playing == "y":
     continue_playing = continue_playing + 1
# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == options[0] and computer_choice == options[1]:
    print("User wins")
elif user_choice == options[1] and computer_choice == options[2]:
    print("Computer wins")
elif user_choice == options[2] and computer_choice == options[0]:
    print("User Wins")
elif user_choice == options[0] and computer_choice == options[2]:
    print("User wins")
else:
        print("Try again")

input("Continue playing ? (y)es or (n)o")
    