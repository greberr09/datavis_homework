This Python script analyzes the records in a two-column input csvfile 
that has Date and Profit/losses columns.  It outputs its final calculations for the overall dataset to
a terminal and also to a text file.  The input file was provided in the subdirectory "Resources," and the output
file is written to the subdirectory "analysis," per the writen requirements.  The program creates the output file
budget_data.txt if the file does not exist, or overwrites the output file contents if it does exist.

The paths are defined as though from the directory where the main.py file is located, and it is assumed that python is 
run from that directory.  To call the program, you have to cd into the appropriate directory and call it usiing Python,
or you can execute it from that directory using a development tool such as VBS studio.

The program calculates:  
	The total number of months included in the dataset, 
	The net total amount of "Profit/Losses" over the entire period, 
	The changes in "Profit/Losses" over the entire period, and the average of those changes
	The greatest increase in profits (date and amount) over the entire period
	The greatest decrease in profits (date and amount) over the entire period

The program makes use of the string, os, and csv modules in Python.

The string formatting and the creation of datatime objects from strings, and printing of datetime objects, are all
derived from multiple searchs of Stack Overflow, the Python documentation, Geeks to Geeks and PYNative, for how to 
handle situations such as missing parts of the dates and how to format the output properly for things like currency.

The program creates several lists from the input data, and also creates two lists, for months and ount of items for that month,
which it updates for each row read, after the header row.  The list creation could be done in different ways, such as applying the list function to the input row and making a list of tuples, but for ease of processing for this application the lists
are separate.  The data set that was provided for testing is quite small.   Probably if this were a huge dataset, a different method of creating the lists
and storing the data would be better.

The program requires certain assumptions about the data, e.g., that it is in provided in chronological order, starting from the earliest date first.  An examination of the data shows that each entry appears to be for one month, and there are
sequential entries for each month from January 2010 to February 2017.

Becasuse the data is provided in a format of "month abbreviation-integer," it is not entirely certain that the assumption about the dates is correct.  The approach here does assume that the differences in 
the entries/rows, which are calculated and stored, are between chronologically-ordered, increasing dates.  If the dates were not sequentially ordered, 
each difference, and consequentially the average difference that the requirements ask to be calculated, would be quite different. If the dates are actually in a different format, suach as month-day, rather than month-year, or the input is not sequential, it would be possible to sort the 
input before processing, which would be fine for this particular dataset but sorting in place for a data set of millions of rows would be much more resource intensive and possibly not practical or possible on a laptop.  More information about the date format would be
on the date format, and what it means, and, even better, a complete date, would be helpful.

The default Python date is Jan 1, 1900 at 00:00:00, and the creation of the date strings depends on using that to set the day of each 
month entry to 1, and the time to midnight.  A different default also could be defined and used for the missing components.
 
