# Import the os module
import os

# Module for reading CSV files
import csv

# Create variables
total_months = 86
total_dollars = 38382578
avg_change = -2315.12
greatest_increase_profit = 1926159
greatest_increase_date = "Feb-2012"
greatest_decrease_profit = -2196167
greatest_decrease_date = "Sep-2013"


# Input csv file
csvpath = os.path.join('', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print('********** csvreader ******************')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print('********** CVS Header ******************')
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)


# Specify the file to write to
output_path = os.path.join("", "Analysis", "financial.txt")

# Open the output file, create a header row, and then write the data contents to the csv
with open(output_path, 'w') as txt_file:

    # Write the output 
    txt_file.write('Financial Analysis')
    txt_file.write('\n')
    txt_file.write('----------------------------')
    txt_file.write('\n')
    txt_file.write(f'Total Months: {total_months}')
    txt_file.write('\n')
    txt_file.write(f'Total: ${total_dollars}')
    txt_file.write('\n')
    txt_file.write(f'Average Change: ${avg_change}')
    txt_file.write('\n')
    txt_file.write(f'Greatest Increase in Profits: {greatest_increase_date}  (${greatest_increase_profit})')
    txt_file.write('\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date}  (${greatest_decrease_profit})')

   
# Print to terminal
    print('********** Print to terminal ******************')
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: {total_dollars}')
    print(f'Average Change: {avg_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_date}  {greatest_increase_profit}')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date}  {greatest_decrease_profit}')

    

# Open the output file in "read" mode ('r') and print to terminal
print('********** Print from the output file ******************')
with open(output_path, 'r') as read_txt:
    print(read_txt.read())


txt_file.close()