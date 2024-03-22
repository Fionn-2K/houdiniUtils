import csv

with open("sentimentdataset.csv", newline="", encoding="uft-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)