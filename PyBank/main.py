#Import modules.
import os
import csv


#create a path to the csv file.
csvpath = os.path.join( ".", "resources","budget_data.csv")

# # #create lists.
# Total_months = []
# Net_total = []
# change = []

# # #open csv file.
with open(csvpath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)


    for row in csvreader:
        print(row)

# # print(csvreader)
# # #     for row in reader:
# # #         Total_months.append(row[0])
# # #         Net_total.append(row[1])
# # # #read header
# # csv_header = next(csvreader)
# # print(f"CSV Header: {csv_header}")



# #Calculate the changes in "profit/loses" over the entire period.
# #Find the average of those changes.


# # #print title for report, begin report here.
# print("\n")
# print("Financial Analysis")
# print("-------------------------")
# # Total_months.pop(0)
# # months = len(Total_months)
# # print("Total Months:" + str(months))
# # Net_total.pop(0)

# # inte_totalr = list(map(int, Net_total))
# # total = sum (inte_totalr)
# # print("Total:" + str(total))

# # for i in range (1, len(inte_totalr)):
# #     change.append(float(inte_totalr[i]-inte_totalr[i-1]))
# #     average_change = round(sum(change)/ len(change), 2)

# # print("Average change: $" + str(average_change))

# # min_value = min(change)
# # max_value = max(change)
# # max_date = str(Total_months[change.index(max_value)+1])
# # min_date = str(Total_months[change.index(min_value)+1])
# # print ("Greatest increase in profits:" + str(max_date) + "$" + str(max_value))
# # print (("Greatest decreate in profits:" + str(min_date) + "$" + str(min_value)))
# print("-------------------------")
# print("\n")
# # for row in csvreader:
# #     print(row)


# #print Greatest Increase in Profits, include the date and amount  over the entire period.
# #Print Greatest Decrease in losses, include the date and amount of the entire period.

# #Export final Script to text file.