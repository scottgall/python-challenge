import csv

with open('resources/budget_data.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  with open('analysis/test.txt', 'w') as new_file:
    fieldnames = ['Profit/Losses']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")

    csv_writer.writeheader()

    for line in csv_reader:
      del line['Date']
      csv_writer.writerow(line)