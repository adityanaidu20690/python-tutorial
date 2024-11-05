import csv
with open("aditya.csv" , "w") as output:
    with open("customers-100.csv") as cs_file:
        data=csv.reader(cs_file , delimiter=",")
        out=csv.writer(output, delimiter=",")
        linecount=0
        for row in data:
            if linecount ==0:
                out.writerow(row)
                linecount +=1
            else:
                out.writerow(row)
                license +=1
        print(f"the number of processed line is {linecount}") 
