# Import the os module
import os

# Module for reading CSV files
import csv

# Declare analysis variables
total_months = 0
previous_amt = 0
total_dollars = 0
first_value = True


# Path to input data
csvpath = os.path.join('', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print("print csvreader.....")
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        date = row[0]
        profit_loss = row[1]

        total_months = total_months + 1

        total_dollars = total_dollars + int(profit_loss)

        if first_value:
            change_amt = 0
            total_change = 0
            change_count = 0
            first_value = False
            greatest_increase_profit = 0
            greatest_increase_date = ""
            greatest_decrease_profit = 0
            greatest_decrease_date = ""
        else:
            change_amt = int(profit_loss) - previous_amt

            total_change = total_change + change_amt

            change_count = change_count + 1

            if change_amt > greatest_increase_profit:
                greatest_increase_profit = change_amt
                greatest_increase_date = date
            if change_amt < greatest_decrease_profit:
                greatest_decrease_profit = change_amt
                greatest_decrease_date = date

        previous_amt = int(profit_loss)

    average_change = "{0:.2f}".format(total_change / change_count)

 
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
    txt_file.write(f'Average Change: ${average_change}')
    txt_file.write('\n')
    txt_file.write(f'Greatest Increase in Profits: {greatest_increase_date}  (${greatest_increase_profit})')
    txt_file.write('\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date}  (${greatest_decrease_profit})')

   
# Open the output file in "read" mode ('r') and print to terminal
with open(output_path, 'r') as read_txt:
    print(read_txt.read())


txt_file.close()

# # Print to terminal
#     print('Financial Analysis')
#     print('----------------------------')
#     print(f'Total Months: {total_months}')
#     print(f'Total: {total_dollars}')
#     print(f'Average Change: {average_change}')
#     print(f'Greatest Increase in Profits: {greatest_increase_date}  {greatest_increase_profit}')
#     print(f'Greatest Decrease in Profits: {greatest_decrease_date}  {greatest_decrease_profit}')