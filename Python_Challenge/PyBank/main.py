# Import needed moduls for filing reading and string formatting

import os
import csv
import string
import statistics
from datetime import datetime

#   Youe task is to create a Python script that analyzes the records to calculate 
#   each of the following values from two column file that has Date and Profit/losses:
#
#   The total number of months included in the dataset
#
#   The net total amount of "Profit/Losses" over the entire period
#
#   The changes in "Profit/Losses" over the entire period, and then the average of those changes
#
#   The greatest increase in profits (date and amount) over the entire period
#
#   The greatest decrease in profits (date and amount) over the entire period

print("pybank assignment")

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# csvpath = "C:\CWRU_Bootcamp\Git\datavis_homework\Python_challenge\PyBank\Resources\budget_data.csv"



# Set variable to check if we found the video
month = ""
amount = 0.00
day = 0

# Open the CSV
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dates = []
    earnings = []
    
    total_earned = 0
    total_months = 0
    day = ""
    cntr= 0


    # Loop through file doing calculations if month changes
    for row in csvreader:
        month_day = row[0].split("-")
        month = month_day[0]
        day = month_day[1]
        earned = float(row[1])
        myDate=datetime.strptime(row[0], "%b-%d")

        total_earned+=earned

        cntr = months.index(month)

        dates.append(myDate)
        earnings.append(earned)

        
        print(row[0] + " " + str(month) + " day " + day +  " earned " + str(earned) + " " + str(cntr))
        print(f"${total_earned:,.2f}")
        print(myDate)
        print(str(myDate.month))

        month_totals[cntr]+=1
          
    


    # Print the final totals
    
    #for mnth in months:
    #   cntr = months.index(mnth)
    # total_months=   print(mnth + str(month_totals))
    total_months = sum(month_totals)

    # Calculate first date of the year

    startDate = min(dates)
    endDate = max(dates)

    startPrice = earnings[dates.index(startDate)]
    endPrice = earnings[dates.index(endDate)]
    items = len(earnings)
    print("items " + str(items))
    # netChange = (endPrice-startPrice)/startPrice * 100
    netChange = (endPrice/startPrice) - 1
    print("net change " + str(netChange))
    
    total_earnings = sum(earnings)

    # Annual growth rate formula = [ending value/ beginning value] - 1
    #How do you calculate average change per year?
    #How to use the annual growth rate formula

    #Find the ending value of the amount you are averaging. ...
    #Find the beginning value of the amount you are averaging. ...
    #Divide the ending value by the beginning value. ...
    #Subtract the new value by one. ...
    #Use the decimal to find the percentage of annual growth.
    #
    #
    #
    avgChange = (endPrice/startPrice) - 1
    print("Average change " + str(avgChange))

    avgChange = endPrice - startPrice
    print("Average change2 " + str(avgChange))

    avgChange = (endPrice - startPrice)/total_earnings
    print("Average change23 " + str(avgChange))

    avgChange = (endPrice - startPrice)/items
    print("Average change4 " + str(avgChange))

    print("total earnings " + str(total_earnings))

    minEarned=min(earnings)
    maxEarned=max(earnings)

    minDate=dates[earnings.index(minEarned)]
    maxDate=dates[earnings.index(maxEarned)]

    print("min " + str(minEarned))
    print(f"min {minDate.month} is day {minDate.day}") 
    print("Max " + str(maxEarned))
    
    print(f"max {maxDate.month} is day {maxDate.day}")

    print(startDate)
    print(endDate)
    print(str(startPrice))
    print(str(endPrice))


    print(f"The total earned for the year ${total_earned:,.2f}\n")

    # print(f"Financial Analysis\n")
    # print(f"=====================\n")
    data=(f"Financial Analysis\n=====================\n")

    
    data+=(f"Total months: {total_months}\n")
    data+=(f"Total: ${total_earned:,.2f}\n")
    data+=(f"Average change: \n")
    data+=(f"Greatest increase in profits: \n")
    data+=(f"Greatest decrease in profits: \n")

    print(data)

# Specify the file to write to
output_path = os.path.join(".", "analysis", "budget_results.txt")

# Open the file using "write" mode. Specify the variable to hold the output
    
with open(output_path, 'w') as txtfile:

# Write the results to a file
# 
# 

    txtfile.writelines(data)
    #txtfile.write(f"Financial Analysis\n")
    #txtfile.write(f"=====================\n")

    #txtfile.write(f"Total months: \n")
    #txtfile.write(f"Total: ${total_earned:,.2f}\n")
    #txtfile.write(f"Average change: \n")
    #txtfile.write(f"Greatest increase in profits: \n")
    #txtfile.write(f"Greatest decrease in profits: \n")



