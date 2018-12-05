# import statements
import os
import csv

# find the csv file budget_data.csv using os library
budgetData = os.path.join("Resources", "budget_data.csv")

# initialize variables
months = 0
mostPos = 0
mostNeg = 0
monthPos = 0
monthNeg = 0
total = 0
totalChange = 0
lastMonth = 0
changes = []
monthList = []

# open budgetData, any newline character as csvfile (csv.reader() and next())
# then remove header
with open(budgetData, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
# Begin traversing file and reading data into lists (I want to close the file asap, can do calculations after)
# Note that I will need to deliberately ignore the value associated with month 0 except when calculating total
# I wanted to use a dictionary here, but I feel like I'd end up splitting it into two lists anyway when calculating stuff
    for row in csvreader:
        changes.append(float(row[1]) - lastMonth)
        monthList.append(row[0])
        lastMonth = float(row[1])

# Now that the file is closed, update variables
# When calculating mostPos, mostNeg, I can use elif() since both values are initialized to 0, can't have something
# both greater than mostPos and less than mostNeg

# Side note: in the for loop, I didn't know if .index() using "in changes" or the way I did it is more efficient
# I did it this way since I figured searching a list would be bad in general, plus it's possible there are two of
# the same value in changes
lastMonth = 0
months = len(monthList)
for m in range(months):
    lastMonth = (changes[m] + lastMonth)
    total += lastMonth
    if (m == 0):
        continue
    if (changes[m] > mostPos):
        mostPos = changes[m]
        monthPos = m
    elif (changes[m] < mostNeg):
        mostNeg = changes[m]
        monthNeg = m
    totalChange += changes[m]

# Sometimes I just feel better reassigning variables like this, especially when changing between types
# "/" should be the __truediv__() method, so hopefully no weird errors?
tempV = totalChange
totalChange = tempV / (months - 1)
tempV = monthPos
monthPos = monthList[tempV]
tempV = monthNeg
monthNeg = monthList[tempV]

# Print to terminal
printStr = ("Financial Analysis\n" + "----------------------------\n" +
           "Total Months: " + str(months) + "\n" + 
           "Total: $" + str(total) + "\n" +
           "Average Change: $" + str(round(totalChange, 2)) + "\n" +
           "Greatest Increase in Profits: " + monthPos + " ($" + str(mostPos) + ")\n" +
           "Greatest Descrease in Profits: " + monthNeg + " ($" + str(mostNeg) + ")")
print(printStr)

# Output to .txt
financial_analysis = os.path.join("Output", "financial_analysis.txt")
with open(financial_analysis, "w") as finAn:
    finAn.write(printStr)
