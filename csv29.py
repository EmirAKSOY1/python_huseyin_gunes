#ıris data
import csv
with open('iris.data',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(csvfile)
    for row in reader:
        print(row)
        print(row["species"])
