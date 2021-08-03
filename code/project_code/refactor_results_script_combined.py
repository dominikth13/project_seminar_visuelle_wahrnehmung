import csv

oldfiles = ['b1','b2','b3','b4','d1','d2','d3','p1','p2','p3']
newfile = 'refactored/combined_data.csv'
Matrix = [0 for y in range(1000)] 
person_count = 1

for id in oldfiles:
    with open('refactored/design_rating_double_results_' + id + '_refactored.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(row)
            Matrix[100*(person_count - 1) + line_count-1] = ["Testperson " + str(person_count),row["reference_image"],row["test_image"],row["img_size"],row["response"],row["resptime"]]
            line_count += 1
    person_count += 1
print(Matrix)

with open(newfile, mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['test_person','reference_image', 'test_image', 'img_size', 'response', 'resptime'])
    for row in Matrix:
        employee_writer.writerow(row)