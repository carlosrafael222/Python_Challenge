#Import modules.
import os
import csv


#create a path to the csv file.
csvpath = os.path.join( ".", "resources","budget_data.csv")

#create lists.
total_months = []
total = []
change = []

 #open csv file.
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total.append(row[1])


# Print final report.
print("\n")
print("Financial Analysis")
print("-------------------------")

# Print The total number of months included in the dataset
total_months.pop(0)
months = len(total_months)
print(f"Total Months:{months}")
total.pop(0)


#The net total amount of "Profit/Losses" over the entire period
net_total = list(map(int, total))
total = sum (net_total)
print(f"Total:{total}")


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
for i in range(1, len(net_total)):
    change.append(float(net_total[i]-net_total[i-1]))
    average_change = round(sum(change)/ len(change), 2)

print(f"Average change:$ {average_change}")

min_value = min(change)
max_value = max(change)
max_date = str(total_months[change.index(max_value)+1])
min_date = str(total_months[change.index(min_value)+1])
print (f"Greatest increase in profits: {max_date} $ {max_value}")
print (f"Greatest decreate in profits: {min_date} $ {min_value}")
print("-------------------------")
print("\n")

# Export final Script to text file.
output_path = os.path.join(".", "Analysis", "budget_analysis.txt")

output_path = open(output_path,"w")

output_path.write("\n")
output_path.write("financial Analysis\n")
output_path.write("----------------------------\n")
output_path.write(f"Total Months {months}\n")
output_path.write(f"Total:{total}\n")
output_path.write(f"Average change ${average_change}\n")
output_path.write(f"Greatest increase in profits: {max_date} $ {max_value}\n")
output_path.write(f"Greatest decrease in profits: {min_date} $ {min_value}\n")
output_path.write("-------------------------\n")

output_path.close()