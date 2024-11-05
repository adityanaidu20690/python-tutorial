import csv

# Open the output file 'aditya.csv' in write mode
with open("aditya.csv", "w", newline='') as output:
    # Open the input CSV file 'customers-100.csv' in read mode
    with open("customers-100.csv") as cs_file:
        # Create a CSV reader object for reading the input file with comma delimiter
        data = csv.reader(cs_file, delimiter=",")
        
        # Create a CSV writer object to write to the output file with comma delimiter
        out = csv.writer(output, delimiter=",")
        
        # Initialize the line counter
        linecount = 0
        
        # Loop through each row in the input CSV data
        for row in data:
            if linecount == 0:
                # For the first row (header), write it to the output file
                out.writerow(row)
                linecount += 1  # Increment linecount for the header row
            else:
                # For all other rows, write the data rows to the output file
                out.writerow(row)
                linecount += 1  # Increment linecount for each data row
                
        # Print the total number of lines processed
        print(f"The number of lines processed is {linecount}")

