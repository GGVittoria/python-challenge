# Import the os module
import os

# Module for reading CSV files
import csv

# Declare analysis variables
total_votes = 0
candidates = {}
winner_vote_count = 0
winner = ""


# Path to input data
csvpath = os.path.join('', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print("print csvreader.....")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        profit_loss = row[1]

        total_votes = total_votes + 1
        name = row[2]

        if name not in candidates:
            candidates[name] = 1
        else:
            candidates[name] = candidates[name] + 1

# Specify the file to write to
output_path = os.path.join("", "Analysis", "election.txt")

# Open the output file, create a header row, and then write the data contents to the csv
with open(output_path, 'w') as txt_file:

    # Write the output 
    txt_file.write('Election Results')
    txt_file.write('\n')
    txt_file.write('----------------------------')
    txt_file.write('\n')
    txt_file.write(f'Total Votes: {total_votes}')
    txt_file.write('\n')
    txt_file.write('----------------------------')
    txt_file.write('\n')

    # print(candidates)

    for candidate_name, vote_count in candidates.items():
        percentage = '{0:.3%}'.format((vote_count / total_votes))
        vote_count = (vote_count)
        
        txt_file.write(f"{candidate_name}: {percentage} ({(vote_count)})")
        txt_file.write('\n')

        if vote_count > winner_vote_count:
            winner_vote_count = vote_count
            winner = candidate_name

    txt_file.write('----------------------------')
    txt_file.write('\n')
    txt_file.write(f'Winner: {winner}')
    txt_file.write('\n')
    txt_file.write('----------------------------')


# Open the output file in "read" mode ('r') and print to terminal
with open(output_path, 'r') as read_txt:
    print(read_txt.read())


txt_file.close()