#Import modules
import os
import csv

#create a path to the csv file
csvpath = os.path.join( "..","resources","budget_data.csv")


#create lists
Total_num_months = []
Net_Total = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    

    #read header
    csvheader = next(csvreader)
    

#Calculate the changes in "profit/loses" over the entire period.
#Find the average of those changes.

# #print title for report, begin report here.
print("Financial Analysis")
print("-------------------------")
print ()
# for row in csvreader:
#     print(row)


#print Greatest Increase in Profits, include the date and amount  over the entire period.
#Print Greatest Decrease in losses, include the date and amount of the entire period.
#Print final script on terminal
#Export final Script to text file.