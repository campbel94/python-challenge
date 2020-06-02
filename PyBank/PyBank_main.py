# Main Bank

# Dependant Modules
import csv
import os

# Set path for file
budget_path = os.path.join('Resources', 'budget_data.csv')

# Open the csv
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    budget_header = next(budget_reader)

    #Define month counter
    month_counter = 0
    #Define the profit/loss counter
    month_list = []
    profit_counter = []

    # Read through each row of data after the header
    # This  will provide us 'Total number of months' and 'Net Profit/Losses'
    for row in budget_reader:
        month_counter = month_counter + 1
        profit_counter.append(int(row[1]))
        month_list.append(row[0])
    print("Financial Analysis")
    print("\n_____________________________________________\n")
    print(f"Total Months: {month_counter}")
    print(f"Net profit/loss: ${sum(profit_counter)}")

    #List for calclating the average change amount
    monthly_change = []
    
    for x, y in zip(profit_counter[0::], profit_counter[1::]):
        monthly_change.append(y-x)
        monthly_change_avg = sum(monthly_change) / len(monthly_change)
        max_increase = max(monthly_change)
        max_decrease = min(monthly_change)
        #monthly_change_enumerated = enumerate(monthly_change)
        max_increase_index = monthly_change.index(max_increase)
        max_decrease_index = monthly_change.index(max_decrease)
        max_increase_int = int(max_increase_index)
        max_decrease_int = int(max_decrease_index)
    print(f"Average monthly change: ${monthly_change_avg}")

    max_month = month_list[max_increase_int+1]
    min_month = month_list[max_decrease_int+1]
    print(f"Greatest increase in profits: {max_month} (${max_increase})")
    print(f"Greatest decrease in profits: {min_month} (${max_decrease})")

    
# Specify the file to write topy
output_path = os.path.join("pybank_output", "PyBank_Output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    csvwriter.writerow(['_______________________________________________________'])

    # Write the next rows
    csvwriter.writerow(['Total Months:', month_counter])
    csvwriter.writerow(['Net profit/loss:', sum(profit_counter)])
    csvwriter.writerow(['Average monthly change:', monthly_change_avg])
    csvwriter.writerow(["Greatest increase in profits:", max_month, max_increase])
    csvwriter.writerow(['Greatest decrease in profits:', min_month, max_decrease])