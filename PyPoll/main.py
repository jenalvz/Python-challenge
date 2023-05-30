# import libraries and dependencies
import os
import csv

#set the path for the CSV file
file_election = "Resources/election_data.csv"

#declare the output file for the final analysis results


# declare variables
total_votes_cast = 0
all_candidates_list = []
stockham_votes = 0
degette_votes = 0
doane_votes = 0
cv={}
cp = {}


with open(file_election) as input_file:
    content = csv.reader(input_file)
    next(content)

    for row in content:
        total_votes_cast = total_votes_cast + 1
        
        candidate = row[2]

        if candidate not in all_candidates_list:
            all_candidates_list.append(candidate)
            cv[candidate] =0
        
        cv[candidate] = cv[candidate] +1


 
# calculate the total number of votes CAST  
print(total_votes_cast)


# calculate a complete list of candidates who received votes 
print(all_candidates_list)

# calc the WINNER based on pop vote

# calc percentage of votes each candidate won
print(cv)

for k in cv:
    v = cv.get(k)
    cp[k] = float(v)/float(total_votes_cast)

print(cp)






