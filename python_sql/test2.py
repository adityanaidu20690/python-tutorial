# reading csv file using python library

# csv_file = open("customers-100.csv")
# for row in csv_file:
#     print(row.split(",")[2])

import csv
with open('customers-100.csv') as csv_file:
    data = csv.reader(csv_file, delimiter = ",")
    linecount=0
    for row in data:
        if linecount ==0:
           print(f"{','.join(row)}")
        #    print(f"this is a cloumn row {row}")
           linecount += 1
        else:
            print(f"there is the date available {','.join(row)}")
            linecount +=1
    print(f"the number of processed line is {linecount}") 