 #import modules.
import os
import csv
from os.path import join

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
            winner = "khan"
        else:
            winner = "li"

num_votes.pop(0)
totalvotes = len(num_votes)

#percentage of votes for each candidate
khanpercent = round (khanvotes/totalvotes * 100, 4)
correypercent = round (correyvotes/totalvotes * 100, 4)
lipercent = round (livotes/totalvotes * 100, 4)
otoolpercent= round (otooleyvotes/totalvotes * 100, 4)

#show winner
print("Election Votes")
print("---------------------")
print("Total Votes:"+ str(totalvotes))
print("---------------------")
print("khan:"+ str(khanpercent) + "%" "(" + str(khanvotes) + ")")
print("Correy:"+ str(correypercent) + "%" "(" + str(correyvotes) + ")")
print("Li:"+ str(lipercent) + "%" "(" + str(livotes) + ")")
print("O'tooley:"+ str(otoolpercent) + "%" "(" + str(otooleyvotes) + ")")

print("--------------------------")
print("Winner:"+ winner)
print("--------------------------")
