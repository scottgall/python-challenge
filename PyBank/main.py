import os
import csv

csv_file = os.path.join("resources", "budget_data.csv")
data_output = os.path.join("analysis", "financial_analysis.csv")

with open(csv_file, 'r', encoding='utf8') as csvfile:
  with open(data_output, 'w', encoding='utf8') as newfile:
    csv_reader = csv.DictReader(csvfile)

    months = 0
    total = 0
    prev_pl = 0
    total_change = 0
    max_inc = 0
    max_dec = 0
    mo = 'Date'
    pl = 'Profit/Losses'

    for line in csv_reader:
      months += 1
      cur_pl = int(line[pl])
      cur_mo = line[mo]
      total += cur_pl
      cur_change = cur_pl - prev_pl
      total_change += cur_change if months != 1 else 0
      if cur_change > max_inc:
        max_inc = cur_change
        max_inc_mo = cur_mo
      elif cur_change < max_dec:
        max_dec = cur_change
        max_dec_mo = cur_mo
      prev_pl = cur_pl
    
    output = f'Financial Analysis\n' \
             f'------------------------\n' \
             f'Total Months: {months}\n' \
             f'Total: ${total}\n' \
             f'Average Change: ${total_change/(months -1):.2f}\n' \
             f'Greatest Increase in Profits: {max_inc_mo} (${max_inc})\n' \
             f'Greatest Decrease in Profits: {max_dec_mo} (${max_dec})\n'

    print(output)
    newfile.write(output)