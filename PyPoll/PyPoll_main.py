# PyPoll main
# Dependant Modules
import csv
import os

# Set path for file
election_path = os.path.join('Resources','election_data.csv')

# Open the csv
with open(election_path) as election_file:
    election_reader = csv.reader(election_file, delimiter=",")
    election_header = next(election_reader)

    row_counter = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in election_reader:
        row_counter = row_counter + 1

        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li":
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

        khan_percentage = '{0:.2f}'.format((khan_votes / row_counter) * 100)
        correy_percentage = '{0:.2f}'.format((correy_votes / row_counter) * 100)
        li_percentage = '{0:.2f}'.format((li_votes / row_counter) * 100)
        otooley_percentage = '{0:.2f}'.format((otooley_votes / row_counter) * 100)

    results = {
        "Khan" : khan_votes,
        "Correy" : correy_votes,
        "Li" : li_votes,
        "O'Tooley" : otooley_votes
    }

    winner = max(results.items(), key=lambda x : x[1])

    print("Election Results")
    print("\n__________________________________\n")
    print(f"Khan: {khan_percentage}% ({khan_votes})")
    print(f"Correy: {correy_percentage}% ({correy_votes})")
    print(f"Li: {li_percentage}% ({li_votes})")
    print(f"O'Tooley: {otooley_percentage}% ({otooley_votes})")
    print("\n__________________________________\n")
    print(f"Winner: {winner[0]}")
    print("\n__________________________________\n")

# Specify the file to write topy
output_path = os.path.join("output", "PyPoll_Output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])

    csvwriter.writerow(['_______________________________________________________'])

    # Write the second row
    csvwriter.writerow(['Khan', khan_percentage, khan_votes])
    csvwriter.writerow(['Correy', correy_percentage, correy_votes])
    csvwriter.writerow(['Li', li_percentage, li_votes])
    csvwriter.writerow(["O'Tooley", otooley_percentage, otooley_votes])
    csvwriter.writerow(['Khan', khan_percentage, khan_votes])

    csvwriter.writerow(['_______________________________________________________'])

    csvwriter.writerow(['Winner', winner[0]])