import csv

with open('resources/budget_data.csv', 'r') as csv_file:
  with open('analysis/test.txt', 'w') as new_file:
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
      cur_change = (cur_pl - prev_pl)
      if cur_change > max_inc:
        max_inc = cur_change
        max_inc_mo = cur_mo
      elif cur_change < max_dec:
        max_dec = cur_change
        max_dec_mo = cur_mo
      # total_change += cur_change
      prev_pl = cur_pl

    output = ('Financial Analysis\n------------------------\n'
              'Total Months: ' + str(months) + '\n'
              'Total: $' + str(total) + '\n'
              'Average Change: $' + '\n'
              'Greatest Increase in Profits: ' + max_inc_mo + ' ($' + str(max_inc) + ')\n'
              'Greatest Decrease in Profits: ' + max_dec_mo + ' ($' + str(max_dec) + ')\n'
              )
    print(output)
    new_file.write(output)