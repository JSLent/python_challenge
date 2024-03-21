import os
import csv

# Path to the election data CSV file
election_csv = os.path.join("..", "python_challenge", "PyPoll", "Resources", "election_data.csv")  # Update with the actual path

# Initialize variables
total_votes = 0
candidate_votes = {}  # Dictionary to store candidate votes

# Read the election data
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  # Candidate name is in the third column
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate candidate statistics
candidates = list(candidate_votes.keys())
candidate_statistics = []
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    candidate_statistics.append((candidate, votes, percentage))

# Determine the winner
winner = max(candidate_statistics, key=lambda x: x[1])

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, percentage in candidate_statistics:
    print(f"{candidate}: {percentage:.2f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")

#specify output path
output_file = os.path.join("..", "python_challenge", "analysis", "election_results.txt")

# Export results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes, percentage in candidate_statistics:
        txt_file.write(f"{candidate}: {percentage:.2f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner[0]}\n")
    txt_file.write("-------------------------\n")

