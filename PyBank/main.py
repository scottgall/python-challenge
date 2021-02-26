import csv

with open('resources/budget_data.csv', 'r') as csv_file:
  with open('analysis/financial_analysis.txt', 'w') as new_file:
    csv_reader = csv.DictReader(csv_file)

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
    new_file.write(output)