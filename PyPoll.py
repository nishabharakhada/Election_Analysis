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
candidate_results = ""
candidate_votes = {'Charles Casper Stockham':0, 'Diana DeGette':0, 'Raymon Anthony Doane':0}
county_votes = {  }

file_to_load = os.path.join("election_results.csv")
with open(file_to_load, 'r') as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        candidate_name = row[2]
        county_name = row[1]
        candidate_votes[candidate_name] += 1
        if county_name in county_votes.keys():
            county_votes[county_name]+=1
        else:
            county_votes[county_name]=1
    

        # if candidate_name not in  candidate_options:
        #     candidate_options.append(candidate_name)
        total_votes += 1
    
print(total_votes)
print(candidate_votes)
print(county_votes)        
winning_percentage, winning_count, winning_candidate  = 0, 0,""  
for k,v in candidate_votes.items():
    vp = round(float(v)/float(total_votes)*100,1)
    candidate_results += (f"{k}: {vp:.1f}% ({v:,})\n")
    print(candidate_results)
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

county_results = ("county_votes:\n")
county_percentage, county_count, county_turnout  = 0, 0,""  
for k,v in county_votes.items():
    vp = round(float(v)/float(total_votes)*100,1)
    county_results += (f"{k}: {vp:.1f}% ({v:,})\n")
    print(county_results)
    if v > county_count:
        county_percentage, county_count, county_turnout  = vp, v,k
    

county_turnout_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {county_turnout}\n"
    f"-------------------------\n")
print(county_turnout_summary)

file_to_save = os.path.join("election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    
    # txt_file.write("Counties in the Election\n")
    # txt_file.write("------------------------\n")
    # txt_file.write("Arapahoe\nDenver\nJefferson")

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(f"-------------------------\n")
    txt_file.write(county_results)
    txt_file.write(county_turnout_summary)
    
    
file_to_save = os.path.join("election_results.txt")
with open(file_to_save, "w") as txt_file:
    
    txt_file.write(winning_candidate_summary)
   
# candidate_results = (f"{candidate_name}: {vp:.1f}% ({candidate_votes:,})\n")
