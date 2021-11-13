# Initial variable to track game play
user_play = "y"

#Set start and last number 
start_num = 0

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_num =  input("How many numbers to loop ?")
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(start_num + int(user_num)) :

        # Print each number in the range
       print(x)

    #take  last value from user_num and start over 
    start_num = x 

    #start_num = start_num + int(user_num)
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")

    
