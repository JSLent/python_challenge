import os
import csv

budget_csv = os.path.join("..", "python_challenge","PyBank", "Resources", "budget_data.csv")

#create a set to store unique months
unique_months= set()

#create total variable to store total
total = 0

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

print(f"Financial Analysis:")
print(f"----------------------------")
print(f"Total Months: {len(unique_months)}")
print(f"Total: ${total:.2f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Max Increase in Profits: {max_increase_date} ${max_increase:.2f}")
print(f"Max Decrease in Profits: {max_decrease_date} ${max_decrease:.2f}")

#specify output path
output_path = os.path.join("..", "python_challenge", "PyBank", "Resources", "financial_analysis.txt")

#open the file with 'write mode'.  specify the variable to hold the output
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis:\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {len(unique_months)}\n")
    txtfile.write(f"Total: ${total:.2f}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Max Increase in Profits: {max_increase_date} ${max_increase:.2f}\n")
    txtfile.write(f"Max Decrease in Profits: {max_decrease_date} ${max_decrease:.2f}\n")
    


