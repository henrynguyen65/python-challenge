import csv
import os

cvspath = os.path.join("..","Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}  

with open(cvspath, 'r') as file:
    csv_reader = csv.reader(file)
    
    header = next(csv_reader)

    for row in csv_reader:
        
        candidate = row[2] # Extract candidate name

      
        total_votes += 1   # Count the total number of votes

        # Update candidate votes
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Initialize variables to find the winner
winner_candidate_votes = 0
winner_candidate = ""

# Print election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate the percentages and find the final winner candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > winner_candidate_votes:
        winner_candidate_votes = votes
        winner_candidate = candidate

print("-------------------------")
print(f"Winner: {winner_candidate}")
print("-------------------------")

# Export the result
output_file = "election_results.txt"
with open(output_file, 'w') as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {winner_candidate}\n")
    output.write("-------------------------\n")
