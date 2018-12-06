# import os and csv
import os
import csv

# build path to data and output
pollData = os.path.join("Resources", "election_data.csv")
pollDataOutput = os.path.join("Output", "analyzed_election_data.txt")

# initialize variables
# using a dictionary this time since I'll never need to reference who voted for someone
votesTotal = 0
winner = ""
printStr = ("Election Results\n" + "-------------------------------")
candidates = {}
winBar = 0

# open data and collect the data to be analyzed, then close file before analysis
# get rid of header first, then collect
# note, not checking to see if someone voted multiple times, so hopefully the poll workers did their thing
with open(pollData, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
        votesTotal += 1

# update the printStr, analyze the data and add it to printStr
# find out the winner, hopefully they didn't tie or whoever got put in the dictionary first will win
printStr = (printStr + "\nTotal Votes: " + str(votesTotal) + "\n-------------------------------")
for candidate in list(candidates.keys()):
    printStr = (printStr +"\n" + candidate + ": " + str(round(candidates[candidate] * 100 / votesTotal, 3)) + "% (" +
               str(candidates[candidate]) + ")")
    if candidates[candidate] > winBar:
        winBar = candidates[candidate]
        winner = candidate
printStr = (printStr + "\n-------------------------------\nWinner: " + winner +
            "\n-------------------------------")

# print printStr to terminal
print(printStr)

# export printStr to text file
with open(pollDataOutput, "w") as file:
    file.write(printStr)

# Done