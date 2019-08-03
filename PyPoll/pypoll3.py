# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
   # (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his
   #  concentration isn't what it used to be.)
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is
    # composed of three columns: `Voter ID`, `County`, and `Candidate`.
    # Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#==================================================================================================
#import
import os
import csv

#==================================================================================================
# dictionary = {}   
# tuple = ()
# lists = []
# integer = 0

#initialize variables
candidates = []
vote_counts = []
num_votes = 0


#==================================================================================================
#set path
datafile = os.path.join('Resources/election_data.csv')


#==================================================================================================
 #opens the CSV file

with open(datafile) as electiondataCSV:
    csvreader = csv.reader(electiondataCSV)
    #skip header
    line = next(csvreader,None)
    #look for votes
    for line in csvreader:
         #add to total number of votes
        num_votes = num_votes + 1
        #candidate voted for
        candidate = line[2]
        #print(candidate)  -- test for data
        #if other votes then add to vote tally
        if candidate in candidates: 
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
         
        #new candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)
           # print(candidates)  -- Test for data
             

#==================================================================================================
#initialize variables in FOR loop
# dictionary = {}   
# tuple = ()
# lists = []
# integer = 0
percentages = []
max_votes = vote_counts[0]
max_index = 0

#find percentage and winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        max_index = count
       
winner = candidates[max_index]
# Print(candidates[1])  -- Testing data


#==================================================================================================
# Print to screen the election results

print('Election Results')
print('----------------------------------')
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print('Winner: ' + str(winner))
print("---------------------------")


print(datafile)

#==================================================================================================
# Output section 

output_file = datafile 
datafile = f"{output_file}pypoll_results.txt"

# Open write file
filewriter = open(datafile, mode = 'w')

# Print to write file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    filewriter.write("---------------------------\n")
    filewriter.write(f"Winner: {winner}\n")
    filewriter.write("---------------------------\n")

# Close file
filewriter.close()
