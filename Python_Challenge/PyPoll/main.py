
# Import needed modules for filing reading and string formatting

import os
import csv
import string

from datetime import datetime

#--------------------------------------------------------------------------
#   This program is designed, per the requirements, to help a small town to modernize its vote-counting process.
#
#   The election data is contained in the folder "Resources," in the  .csv file "election_data.csv". 
# 
#   Each row in the election data has three columns: "Ballot ID", "County", and "Candidate". 
# 
#   This Python script reads the data one row at a time, analyzes the votes, and calculates each of the following:
#
#       The total number of votes cast
#       A complete list of candidates who received votes
#       The percentage of votes each candidate won
#       The total number of votes each candidate won
#       The winner of the election based on popular vote
#
#   The program outputs the election result calculations to the terminal and also 
#   exports them to a text file.  Per requirements, that file is in the folder "analysis".  
#   It is called "election_results.txt," and will be created if necessary or overwritten
#   if it already exists in the folder.
# #---------------------------------------------------------------------------

# Set path for input file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# -----------------------------------
# Open the CSV file.  Using "with open" means that
# the file will be closed automatically at the end of the indent block
# -----------------------------------

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first and don't do calculations on it

    csv_header = next(csvreader)
    
    # -----------------------------------
    # initialize variables.  This might not be very "Pythonic," but I think it helps the reader
    # to know what is going on and helps coders to think about type checking and missing values.
    # -----------------------------------
    
    # The list of candidate names, which indexes to the votes

    candidates = []

    # the votes list stores a vote total per candidate

    votes = []
 
    candidateVotes = 0
    electionTotal = 0
    candidatePercent = 0.0
    maxVotes = 0
    cntr = 0
    num_cands = 0

    winner= ""
    candidateName = ""
    ballotId = ""
    candidate = ""
    county = ""

    # -----------------------------------
    # Loop through file checking if the candidate is in the dictionary.
    # if not, add the candidate to the dictionary and start adding to that candidate's
    # vote count.   If yes, add the vote to the existing candidate total.
    # The candidate's total number of votes and that candidate's percentage of the 
    # the total votes in the election are calculated after all of the rows have been read.
    # -----------------------------------

    for row in csvreader:

        # Get the data for this row
        # Ballot and county information are not used in
        # this application, after they are collected in variables, but might be in 
        # another such as examining for possible voter fraud.
        
        ballotId = row[0]
        county = row[1]
        candidate = row[2]

        # if the candidate's name is not in the list, add it.
        # Add a vote total for this candidate and set it to 0

        if candidate not in candidates:
            candidates.append(candidate)
            votes.append(0)

        # Whether just added or already existing, this
        # Candidate is now in the list of candidates, get index
        # and increment the vote count

        canIdx = candidates.index(candidate)
        
        votes[canIdx]+=1
        
        # reset for next row

        candidateName = ""
        ballotId = ""
        candidate = ""
        county = ""
        percent_str = ""
          
    # end of reading rows in input file

       
    #-----------------------------------
    # Calculate totals for this dataset
    #-----------------------------------
    
    electionTotal = sum(votes)

    maxVotes = max(votes)
    winner = candidates[votes.index(maxVotes)]

    #-----------------------------------
    # print the title information for the output
    #-----------------------------------
    
    data=(f"\nElection Results\n=========================\n")
    
    # print the total votes

    data+=(f"-------------------------\n")
    
    data+=(f"Total votes: {electionTotal:,.0f}\n")

    data+=(f"-------------------------\n\n")
    

    # loop through the candidates list and print the results for each

    num_cands = len(candidates)

    for cntr in range(0, num_cands):

        # calculate the percent of votes for this candidate

        candidateVotes = votes[cntr]
        candidatePercent = candidateVotes/electionTotal * 100

        # Add this candidate's information to the output.
        # The string formattins is from multiple searches of StackOverflow, Python documentation,
        # and Geeks to Geeks.  Create the percent string outside the f-string because of restriction
        # on having quotation marks inside the curly brackets.  

        percent_str = "{0:.3f}%".format(candidatePercent) 

        data+=(f"{candidates[cntr]}:  {percent_str}  ({candidateVotes:,.0f}) \n\n")

    
    # Add the winner information at the end

    data+=(f"-------------------------\n")
    data+=(f"Winner:  {winner}  \n")
    data+=(f"-------------------------\n")


    # display results to terminal

    print(data)

#-----------------------------------
# Specify the file to write to
#-----------------------------------

output_path = os.path.join(".", "analysis", "election_results.txt")

#-----------------------------------
# Open the file using "write" mode. Specify the variable to hold the output.
# If the file does not exist, it will be created.  If it exists, any contents will be overwritten.
# The file will close automatically after the end of the with open block.
#-----------------------------------
    
with open(output_path, 'w') as txtfile:

#-----------------------------------
# Write the same results to the output file as were printed to the terminal
#-----------------------------------

    txtfile.writelines(data)
