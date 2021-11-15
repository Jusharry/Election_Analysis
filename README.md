# Election_Analysis

## Project Overview
The purpose of this election audit analysis was to determine and return the outcomes of a recent congressional election with focus on the largest voter turnouts by county and the overall winner of the election.

## Election-Audit Results

* Total number of votes cast : 369,711

#### Number and percentage of votes by county :

* Arapahoe - 24,801 (6.7%)

* Denver - 306,055(82.8%)

* Jefferson - 38,855(10.5%)

* Denver county had the largest number of votes

#### Number and percentage of votes per candidate :

* Charles Casper Stockham received 85,213 votes (23.0)% of the total vote.

* Diana DeGette received 272,892 votes (73.8)% of the total vote.

* Raymon Anthony Doane received 11,606 votes (3.1)% of the total vote.

The winner of the election by popular vote was :

  Diana DeGette  with 272,892 votes and 73.8% of the votes cast


## Code references

[Variable Assignment](https://github.com/Jusharry/Election_Analysis/blob/61b2dc3130a41ec22b8119718795099c336fecb0/Resources/%20variable_assignment.png)

[County Votes](https://github.com/Jusharry/Election_Analysis/blob/61b2dc3130a41ec22b8119718795099c336fecb0/Resources/county_votes%20screenshot.png)

[Candidate Votes](https://github.com/Jusharry/Election_Analysis/blob/8bd6b7165eca177a727e340308984ba4c323bb86/Resources/winning_candidate.png)



## Summary 
While this script has been used to return results for this election , I firmly believe that the scope is much broader . I can show that the script can be modified to capture data for a result at the state or country level where the counties can be measured for their  individual contributions to the candidates which can further be used to plan rallies in the strongest states and reveal which areas need extra attention.

- Add list of states

states = []

county_list = []

county_votes = {}

 - Use total votes to determine voter turnout 

    for row  in reader :

        total_votes= total_votes + 1 

        states_turnout = total_votes

- Add list of counties to appropriate state

    if county_list not in states:

        states.append(county_list)




    
