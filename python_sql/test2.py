# reading csv file using python library

# csv_file = open("customers-100.csv")
# for row in csv_file:
#     print(row.split(",")[2])

import csv

# Open the CSV file for reading
with open('customers-100.csv') as csv_file:
    # Create a CSV reader object and set delimiter as comma
    data = csv.reader(csv_file, delimiter=",")
    
    linecount = 0  # Initialize the counter for the lines processed
    
    # Iterate through each row in the CSV file
    for row in data:
        if linecount == 0:
            # Print the header row (first line in the CSV)
            print(f"Header row: {','.join(row)}")
            linecount += 1  # Move to the next line after printing header
        else:
            # Print the data rows (every row except the header)
            print(f"Data row: {','.join(row)}")
            linecount += 1  # Increment the line counter for each row
    
    # Print the total number of processed lines (header + data rows)
    print(f"Total number of lines processed: {linecount}")
