# Reading a CSV file in Python without using a CSV library

# Open the CSV file for reading
csv_file = open('customers-100.csv')

# Loop through each row in the file
for row in csv_file:
    # Split each row by comma and print the second element (index 1)
    # The assumption is that the second column contains the data of interest
    print(row.split(",")[1])

# Close the CSV file after reading
csv_file.close()
