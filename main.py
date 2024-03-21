import os
import csv

# Path to the budget data CSV file
budget_csv = os.path.join("..", "python_challenge","PyBank", "Resources", "budget_data.csv")
# Path to the election data CSV file
election_csv = os.path.join("..", "python_challenge", "PyPoll", "Resources", "election_data.csv")

#create a set to store unique months
unique_months= set()

#create total variable to store total
total = 0

#create total vote variable to store total
total_votes = 0

#dictionary to store candidate votes
candidate_votes = {}  

#create variables to store the total change and previous rows value, max increase and max decrease and dates
total_change = 0
prev_value = None
max_increase = float('-inf')
max_decrease = float('inf')
max_increase_date = None
max_decrease_date = None

#counter for number of changes

num_changes = 0

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader) #skip header row
    month_index = csv_header.index("Date") #get index of the date column
    total_index = csv_header.index("Profit/Losses") #get index of the profit/losses column
    average_change = csv_header.index("Profit/Losses")

    for row in csv_reader:
        unique_months.add(row[month_index])
        total += float(row[total_index]) #change value to float before adding it to the total
        value = float(row[average_change]) #change to float
        date = row[month_index] #get the date
    
        if prev_value is not None: #skip first row bc no previous
            change = value - prev_value #calculate change from prev row
            total_change+= change #add the change to the total change
            num_changes += 1 #increment the counter

            #check if the change is a new max increase or max decrease
            if change > max_increase:
                max_increase = change
                max_increase_date = date
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = date

        prev_value = value #update prev row value

#calculate avg change
average_change = total_change/num_changes

#print results to terminal
print(f"Financial Analysis:")
print(f"----------------------------")
print(f"Total Months: {len(unique_months)}")
print(f"Total: ${total:.2f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Max Increase in Profits: {max_increase_date} ${max_increase:.2f}")
print(f"Max Decrease in Profits: {max_decrease_date} ${max_decrease:.2f}")

#specify output path
output_path = os.path.join("..", "python_challenge", "analysis", "financial_analysis.txt")

#open the file with 'write mode'.  specify the variable to hold the output
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis:\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {len(unique_months)}\n")
    txtfile.write(f"Total: ${total:.2f}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Max Increase in Profits: {max_increase_date} ${(max_increase):.2f}\n")
    txtfile.write(f"Max Decrease in Profits: {max_decrease_date} ${(max_decrease):.2f}\n")

#Read the election data
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  # Candidate name is in the third column
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

#calculate candidate stats
candidates = list(candidate_votes.keys())
candidate_statistics = []
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    candidate_statistics.append((candidate, votes, percentage))

#determine winner
winner = max(candidate_statistics, key=lambda x: x[1])

#print results to terminal
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

#export results to text file
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

