import csv
import os

oldfile = input("Dateinamen hier eingeben (inkl. .csv):")
newfile = oldfile.split(".")[0] + "_refactored.csv"
Matrix = [0 for y in range(100)] 
		

with open(oldfile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        Matrix[line_count-1] = [row["reference_image"][5:7],row["test_image"].split("/")[1][1:],os.path.getsize(row["test_image"]),row["response"],row["resptime"]]
        line_count += 1
    print(Matrix)

with open(newfile, mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['reference_image', 'test_image', 'img_size', 'response', 'resptime'])
    for row in Matrix:
        employee_writer.writerow(row)
    
