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

#Print the total votes 
print(candidate_votes)

for candidate_name in candidate_votes :
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) *100
    print (f"\n{candidate_name} received {votes} ({vote_percentage:.1f})% of the total vote.") 
    #Determine the winning votes and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage) :
        winning_count = votes 
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
print (f'---------------------------\nThe candidate {winning_candidate} has won the election with {winning_count} votes and by {winning_percentage:.1f}% of the votes.')

#perform analysis
# #pseudocode start 
# 1. Count total number of votes cast 
# 2. Make a complete list of candidates who received votes 
# 3. Count total number of votes that each candidate received 
# 4. Calculate the percentage of votes that each candidate won 
# 5. Determine the election winner based on popular vote

