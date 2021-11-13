#candidate_votes = int(input("How many votes did the candidate get in the election?"))
#total_votes = int(input("What is the total number of votes in the election?"))
# message_to_candidate = (f"You received {candidate_votes}  of votes."
#                         f"The total number of votes in the election was {total_votes}."
#                         f"You received {candidate_votes/total_votes * 100:.2f} % of the total votes.")

counties_dict = {"Arapahoe" : 422829, "Denver" :463353, "Jefferson" : 432438}
voting_data = [{"county" : "Arapahoe", "registered_voters": 42289},
                {"county" : "Denver", "registered_voters": 463353},
                {"county" : "Jefferson", "registered_voters":432438}]

#print(message_to_candidate)

# for county in counties_dict.keys() :
#     print(county)
# for voters in counties_dict.values() :
#     print(voters)
# for county in counties_dict:
#     print (counties_dict[county])
# for county in counties_dict :
#     print(counties_dict.get(county))

for county, voters in counties_dict.items() : 
    print(f" {county} county has  {voters:2,} registered voters.")

#use range()to get a list of dictionaries 
# for county_dict in range(len(voting_data)):
#     print(voting_data[county_dict])
#use nested for loos to get values from dictionary
# for county_dict in voting_data:
#     # for value in county_dict.values():
#     #     print (value)
#         print(county_dict["registered_voters"])
# #using f strings
# for county, voters in counties_dict.items() : 
#     print(f"{county} county has {voters} registered voters.")

