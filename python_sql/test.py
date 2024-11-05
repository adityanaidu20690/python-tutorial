# reading csv file using python without using python library
csv_file = open('customers-100.csv')
for row in csv_file:
    print(row.split(",")[1])