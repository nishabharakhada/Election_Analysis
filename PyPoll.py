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

print(dir(int))
print(dir(float))
print(dir(bool))
print(dir(list))
print(dir(tuple))
print(dir(dict))
print(dir(dt))

print(dir(random))
print(dir(numpy))


file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load, 'r') as election_data:
    print(election_data)
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)


file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")