# import libraries and dependencies
import os
import csv

#set the path for the CSV file
file_election = "Resources/election_data.csv"


# declare variables
total_votes_cast = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

#open the file abd begin reading the data
with open(file_election) as input_file:
    poll_data = csv.reader(input_file)
    next(poll_data)


#calculate total number of votes cast for each candidate
    for row in poll_data:
        total_votes_cast += 1
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif (row[2] == "Diana DeGette"):
            degette_votes += 1
        elif (row[2] == "Raymon Anthony Doane"):
            doane_votes += 1

#calculating candidates' percentages
percent_stockham = round(100 * stockham_votes/total_votes_cast, 3)
percent_degette = round(100 * degette_votes/total_votes_cast, 3)
percent_doane = round(100 * doane_votes/total_votes_cast, 3)

#create candidate dictionary with their names and election results
all_candidates = {'Charles Casper Stockham': percent_stockham,
                  'Diana DeGette': percent_degette,
                  'Raymon Anthony Doane': percent_doane}

#declare winner by higest %, test by printing the winner name in terminal, and them commenting out
winner = max(all_candidates, key=all_candidates.get)
# print(winner)

# print(total_votes_cast)
# print(stockham_votes)
# print(percent_stockham)
# print(degette_votes)
# print(percent_degette)
# print(doane_votes)
# print(percent_doane)
# print(winner)

# time to create a txt file with the analysis and results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes_cast}
-------------------------
Charles Casper Stockham: {percent_stockham}% ({stockham_votes})
Diana DeGette: {percent_degette}% ({degette_votes})
Raymon Anthony Doane: {percent_doane}% ({doane_votes})
-------------------------
Winner: {winner}
-------------------------

"""

print(output)

#create a separate text file with the final result
with open("Analysis/pypoll_output.txt", "w") as txt_file:
    txt_file.write(output)



