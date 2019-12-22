# 
import csv
import os

# Set initial values for calculations
total_votes = 0
candidate_list_with_votes = 0
candidate_percent_votes = []
candidate_total_votes = []
election_winner = []

# Define name for CSV file
file_to_load = os.path.join("election_data.csv")
with open (file_to_load) as voting_analysis:
    csvreader = csv.reader(voting_analysis, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        # Tells me that "row" is the first column
        #print(row)
        # Tells me that "row[1] is the second column"
        #print(row[1])

        # Add to the total by an increment (+=) of 1
        total_votes += 1
       





print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#print(f"Khan: 63.000% (2218231)")
#print(f"Correy: 20.000% (704200)")
#print(f"Li: 14.000% (492940)")
#print(f"O'Tooley: 3.000% (105630)")
#print("-------------------------")
#print(f"Winner: Khan")
#print("-------------------------")