# Module 3 Challenge
# Financial and Election Analysis

----------------------------------

# Overview
This Python script conducts financial and election analyses using provided CSV files. 

The financial analysis includes processing budget data to derive insights such as total months, total profit/losses, average change, and identifying periods of maximum increase and decrease in profits. 

The election analysis looks at voting data to determine the total number of votes cast, each candidate's total votes, their percentage of total votes, and declares the winner of the election.

# Requirements
Python 3
CSV files containing financial and election data

# Financial Analysis
Path to Budget Data: The script assumes that the financial data is stored in a CSV file named budget_data.csv.
Unique Months: The script calculates the total number of unique months included in the dataset.
Total Profit/Losses: It calculates the net total amount of profit/losses over the entire period.
Average Change: Calculates the average of the changes in profit/losses over the entire period.
Greatest Increase and Decrease: Identifies the greatest increase and decrease in profits over the entire period with the corresponding dates.

# Election Analysis
Path to Election Data: The script assumes that the election data is stored in a CSV file named election_data.csv.
Total Votes Cast: The script calculates the total number of votes cast in the election.
Candidate Statistics: It determines the total number of votes each candidate received, their percentage of the total votes cast, and compiles this information into a list.
Winner Determination: Declares the candidate with the highest number of votes as the winner of the election.

# Output
The results of both analyses are printed to the terminal.
Additionally, the results are saved in text files (financial_analysis.txt and election_results.txt) within the analysis directory.

# Usage
Ensure Python 3 is installed on your system.
Place the CSV files containing financial and election data in their respective directories (PyBank/Resources and PyPoll/Resources).
Run the Python script in your terminal:
Copy code
python main.py
The results will be displayed in the terminal and saved in text files.

# Note
This script utilizes the csv module to read CSV files and does not require any external dependencies beyond the Python standard library.