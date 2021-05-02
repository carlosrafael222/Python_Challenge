 #import modules.
import os
import csv


#create a path to the csvfile.
csvpath = os.path.join( ".", "resources", "election_data.csv")

num_votes = []
num_candidates =[]
num_counties = []

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        num_votes.append(row[0])
        num_counties.append(row[1])
        num_candidates.append(row[2])

#count the number of votes
khanvotes = num_candidates.count("Khan")
correyvotes = num_candidates.count("Correy")
livotes = num_candidates.count("Li")
otooleyvotes =num_candidates.count("O'Tooley")

if otooleyvotes > correyvotes:
    if otooleyvotes > khanvotes:
        if otooleyvotes > livotes:
            winner = "O'Tooley"
        else:
            winner = "li"
        
    else: 
        if khanvotes > livotes:
            winner = "Khan"
        else:
            winner= "Li"

else:
    if correyvotes > khanvotes:
        if correyvotes > livotes:
            winner = "Correy"
        else:
            winner = "Li"
    else:
        if khanvotes > livotes:
            winner = "Khan"
        else:
            winner = "li"

num_votes.pop(0)
totalvotes = len(num_votes)


#percentage of votes for each candidate
khanpercent = round (khanvotes/totalvotes * 100)
correypercent = round (correyvotes/totalvotes * 100)
lipercent = round (livotes/totalvotes * 100,)
otoolpercent= round (otooleyvotes/totalvotes * 100)

#show winner
print("Election Votes")
print("---------------------")
print(f"Total Votes:{totalvotes}")
print("---------------------")
print(f"khan:{khanpercent} % ({khanvotes})")
print(f"Correy:{correypercent} %({correyvotes})")
print(f"Li:{lipercent} % ({livotes})")
print(f"O'tooley:{otoolpercent}% ({otooleyvotes})")

print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Export final script to text file
output_path = os.path.join( ".", "Analysis", "Poll_Analysis.txt")

output_path = open(output_path, "w")

output_path.write("\n")
output_path.write("Election Votes\n")
output_path.write("---------------------\n")
output_path.write(f"Total Votes:{totalvotes} \n")
output_path.write("---------------------\n")
output_path.write(f"khan:{khanpercent} % ({khanvotes})\n")
output_path.write(f"Correy:{correypercent} %({correyvotes})\n")
output_path.write(f"Li:{lipercent} % ({livotes})\n")
output_path.write(f"O'tooley:{otoolpercent}% ({otooleyvotes})\n")

output_path.write("--------------------------\n")
output_path.write(f"Winner: {winner}\n")
output_path.write("--------------------------\n")

output_path.close()

