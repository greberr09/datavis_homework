# Import needed modules for filing reading and string formatting

import os
import csv
import string

from datetime import datetime

#--------------------------------------------------------------------------
#   This Python script analyzes the records in a two-column csvfile 
#   that has Date and Profit/losses colums.  The program calculates:
#
#   The total number of months included in the dataset
#
#   The net total amount of "Profit/Losses" over the entire period
#
#   The changes in "Profit/Losses" over the entire period, and  the average of those changes
#
#   The greatest increase in profits (date and amount) over the entire period
#
#   The greatest decrease in profits (date and amount) over the entire period
#---------------------------------------------------------------------------

# Set path for input file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# -----------------------------------
# Open the CSV file.  Using with open means that
# the file will be closed automatically at the end of the indent block
# -----------------------------------

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first and don't do calculations on it

    csv_header = next(csvreader)
    
    # -----------------------------------
    # initialize variables.  This might not be very "Pythonic," but I think it helps reader
    # to know what is going on and helps coders to think about type checking and missing values
    # -----------------------------------
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # The month_day list is for processing the split string from the "may-10" input format

    month_day = []

    #--------------------------------------------------------------------
    # the dates and earnings lists are for input data.  This could be done
    # different ways, such as applying the list function to the input row and making
    # a list of tuples, but for ease of processing for this application the lists
    # are separate.
    #--------------------------------------------------------------------

    dates = []
    earnings = []

    # the diffs list stores a calculated set of differences in earnings from 
    # one month to the next.

    diffs = []
    
    earned = 0.0
    total_earned = 0.0
    total_months = 0.0
    priorEarnings = 0.0
    maxDiff = 0.0
    minDiff = 0.0
    diff = 0.0
    cntr= 0
    do_diff = False

    month =""
    maxDate = ""
    minDate = ""

    # -----------------------------------
    # Loop through file doing calculations on each entry
    # in this dataset.  It appears that each entry is a month
    # and the entries are sequential increasing in month and year.
    # With only two parts of the date, it is not entirely certain 
    # that is correct.  The approach here does assume that the differences
    # in entry are between chronologically-ordered, increasing dates.
    # If the dates were not sequentially ordered, the averaage difference
    # in change in earnings would be very different.  If this is another form 
    # of date, or the input is not sequential, it would be possible to sort the 
    # input before processing, but more information about the date format would be
    # needed.  The default Python date is Jan 1, 1900 at 00:00:00, 
    # and the creation of the date strings depends on using that.  A different
    # default also could be defined and used for the missing components.
    # -----------------------------------

    for row in csvreader:
        month_day = row[0].split("-")
        month = month_day[0]
        earned = float(row[1])

        # The datetime object conversion from string used multiple searches of StackOverflow, 
        # Python documentation, and Geeks to Geeks websites.  For this initial application,
        # it would be possible to simply store as strings, but for any proper sorting
        # or other date calculations, a datetime object is needed.
    
        myDate=datetime.strptime(row[0], "%b-%y") 
        
        # Don't consider the first row to be a difference from the prior state,
        # as it sets the initial state, so start differences at the second row.
        # Calculate the difference in earnings for all subsequent months and
        # add it to the list of differences.

        if do_diff == True:
            diff = earned - priorEarnings
            diffs.append(diff)  

        #  Get the maximum increase for the data set
        #  Store the date as a string for ease of printing to output

        if diff > maxDiff:
            maxDiff = diff
            maxDate = row[0]

        #  Get the maximum decrease for the data set

        if diff < minDiff:
            minDiff = diff
            minDate = row[0]

        # get the index to the list of totals items for each month.
        # A datetime property of month() also could be used to do this,
        # with the additional step of subtracting one from the month number

        cntr = months.index(month)

        # add the input row data to the lists

        dates.append(myDate)
        earnings.append(earned)
   
        # keep totals of items for this particular month

        month_totals[cntr]+=1

        # keep previous difference for comparison to next row

        priorEarnings = earned

        # Set to true after the first data row

        do_diff = True
          
    # end of reading rows in input file

    #-----------------------------------
    # Calculate totals for this dataset
    #-----------------------------------
    
    total_months = sum(month_totals)
    total_earnings = sum(earnings)

    # calculate the average of all of the changes in profits and losses

    avgChange = (sum(diffs)/len(diffs))

    #-----------------------------------
    # print the title information for the output
    #-----------------------------------
    
    data=(f"Financial Analysis\n=====================\n")

    #-----------------------------------
    # print the total amounts for the period.  The formatting is
    # from multiple searches of StackOverflow, Python documentation,
    # and Geeks to Geeks.  
    #-----------------------------------
    
    data+=(f"Total months: {total_months}\n")
    data+=(f"Total: ${total_earnings:,.2f}\n")
    data+=(f"Average change:  ${avgChange:,.2f} \n")
    data+=(f"Greatest increase in profits:  {maxDate} ( ${maxDiff:,.2f} ) \n")
    data+=(f"Greatest decrease in profits:  {minDate} ( ${minDiff:,.2f} ) \n")

# display to terminal

    print(data)

#-----------------------------------
# Specify the file to write to
#-----------------------------------

output_path = os.path.join(".", "analysis", "budget_results.txt")

#-----------------------------------
# Open the file using "write" mode. Specify the variable to hold the output.
# If the file does not exist, it will be created.  If it exists, existing data will be overwritten.
# The file will close automatically after the end of the with open block.
#-----------------------------------
    
with open(output_path, 'w') as txtfile:

#-----------------------------------
# Write the same results to the output file as printed to the terminal
#-----------------------------------

    txtfile.writelines(data)
