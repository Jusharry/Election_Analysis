import csv
import os 
#create a filename variable with a direct or indirect path to a file to open 
file_to_load = os.path.join("Resources","election_results.csv")

#create a filename variable to a direct /indirect path to an output file
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize the total vote counter 
total_votes = 0
#Find the list of candidates 
candidate_otions = []
#create a candidates dictionary 
candidate_votes = {}
#Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0
# Open the election results and read the file 
with open(file_to_load,) as election_data:
   # print(election_data)

#To do : read and analyze the data 
    file_reader = csv.reader(election_data)
#Read and print the headers row 
    header = next(file_reader)
    #print(header)
#Print each row in csv file 
    for row in file_reader:
#add to the total vote count 
        total_votes += 1
        candidate_name = row[2]

#check for and then add canidate name to options
        if candidate_name not in candidate_otions :
#add candidate name to candidate options list 
            candidate_otions.append(candidate_name)
#start tracking candidate votes 
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#using the open() function with 'w' will write data to the file
with open(file_to_save,'w') as text_file:
    #Print final vote count 
    election_results = (
        f"\n Election Results\n"
        f"-------------------------\n"
        f"Total Votes ; {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end = "")

    #save the results to the text file 
    text_file.write(election_results)

    #Print the total votes 
    #print(candidate_votes)

    for candidate_name in candidate_votes :
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        candidate_results = (f"\n{candidate_name} received {votes} votes ({vote_percentage:.1f})% of the total vote.\n") 
        print(candidate_results)
        text_file.write(candidate_results)

    
        #Determine the winning votes and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count : {winning_count}\n"
        f"Winning Percentage : {winning_percentage:.1f}\n"
        f"--------------------------------\n")
    
    print (winning_candidate_summary)
    text_file.write(winning_candidate_summary)





    #perform analysis
    # #pseudocode start 
    # 1. Count total number of votes cast |/
    # 2. Make a complete list of candidates who received votes |/
    # 3. Count total number of votes that each candidate received |/ 
    # 4. Calculate the percentage of votes that each candidate won |/
    # 5. Determine the election winner based on popular vote |/

