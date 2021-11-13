import csv
import os 
#create a filename variable with a direct or indirect path to a file to open 
file_to_load = os.path.join("Resources","election_results.csv")

#create a filename variable to a direct /indirect path to an output file
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file 

with open(file_to_load,) as election_data:
   # print(election_data)

#To do : read and analyze the data 
    file_reader = csv.reader(election_data)
#Read and print the headers row 
    header = next(file_reader)
    print(header)
#Print each row in csv file 
    # for row in file_reader:
    #     print(row)


#perform analysis
# #pseudocode start 
# 1. Count total number of votes cast 
# 2. Make a complete list of candidates who received votes 
# 3. Count total number of votes that each candidate received 
# 4. Calculate the percentage of votes that each candidate won 
# 5. Determine the election winner based on popular vote

