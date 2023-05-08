This Python script is designed, per the requirements, to help a small town modernize its vote-counting process.

The program reads in a csv file of voting information, calculates information about the votes for each candidate, 
calculates election totals, and prints the results to the terminal and also to a text file.

For purposes of this assignment, the input .csv file, named "election_data.csv," is in the folder "Resources," as specified in the requirements, 
and the output file, named "election_results.txt," is created in the folder "analysis."  If the output file does not exist, the script creates the file; 
if the file does exist, the contents are overwritten.   Both input and output files are contained in the PyPoll folder which holds the main
excutable file "main.py."  The election data input file is 369,711 vote entries plus a header.  The file is too big to view in the GIT GUI, and had to be
pushed to the GIt repository through the terminal interface.  If someone tries to view the folder through the GIT GUI, it will generate
a warning message that the file is too large for current GUI viewing.

---------------------------------------------------------------------------------------------------------------
The path structure and the way that the repository is installed expect that the program will be run after changing
into the directory where the main.py is located.   The program MUST be run from that directory only.
----------------------------------------------------------------------------------------------------------------

The input data contains three columns: "Ballot ID", "County", and "Candidate."   For this assignment, although the ballot id and county
are read into variables, only the candidate name is used in calculations.  If the town later wanted to have programming to
identify voter fraud or to determine where more polling places are needed, the county and ballot ID information could be used.

The script reads in one row at a time from the votes file, appends an item to a list if that candidate has had no previous votes, and updates vote counts.
When the entire file has been read, the script analyzes the votes and calculates each of the following:

       The total number of votes cast
       A complete list of candidates who received votes
       The percentage of votes each candidate won
       The total number of votes each candidate won
       The winner of the election based on popular vote

The script creates an output string of this information to be used in both printing to the terminal and writing to the
output file. 

Because the reading and writing are each done with a "with open" statement, the input and output files will close automaticcaly
at the end of the indented code block.

Despite the large file size and writing components of each incoming row to a list, the script runs very quickly, as it is not doing
doing any sorting and does most of its calculations, other than a few counts, after all of the input data has been read in.

There are multiple ways this data could be read in and stored in list, tuple, or dictionary form in order to use the candidate name as a key to add to or
lookup candidate vote totals.  This would probably be a good application for a Panda dataframe, but that is out of scope
for this assignment.


