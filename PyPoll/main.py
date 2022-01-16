# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define variables
voters_candidates = []
votes_per_candidate = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect election data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv file
with open(election_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csvheader = next(csvfile)

    for row in csvreader:

        voters_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

    #sorted_list = sorted(voters_candidates, reverse=True) 
    #sorted_list.sort(reverse=True) 

    # For key, group in groupby(sorted_list):
    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    # Count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # Calculate the percentage of votes per candidate, round to 3 digits
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    #print(c.most_common())
    #print(c.values())
    #print(c.keys())
    #print(sum(c.values()))
    
# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner: {votes_per_candidate[0][0][0]}")
print("-------------------------")


# -->>  Export a text file with the results
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")    

