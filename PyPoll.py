# Pseudo Code:
#  Data to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Import dependencies packages
import datetime as dt
import csv
import os
import random, numpy
curr_time = dt.datetime.now()
print(curr_time)

# print(dir(int))
# print(dir(float))
# print(dir(bool))
# print(dir(list))
# print(dir(tuple))
# print(dir(dict))
# print(dir(dt))

# print(dir(random))
# print(dir(numpy))

total_votes = 0
# candidate_options = []
candidate_votes = {'Charles Casper Stockham':0, 'Diana DeGette':0, 'Raymon Anthony Doane':0}
file_to_load = os.path.join("..","Resources", "election_results.csv")
with open(file_to_load, 'r') as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        candidate_name = row[2]
        candidate_votes[candidate_name] += 1
        # if candidate_name not in  candidate_options:
        #     candidate_options.append(candidate_name)
        total_votes += 1
    
print(total_votes)
print(candidate_votes)
winning_percentage, winning_count, winning_candidate  = 0, 0,""  
for k,v in candidate_votes.items():
    vp = round(float(v)/float(total_votes)*100,1)
    if v > winning_count:
        winning_percentage, winning_count, winning_candidate  = vp, v,k
    print(f"{k}: received {vp}% of the vote.")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    # print(candidate_options)


file_to_save = os.path.join("..","analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
