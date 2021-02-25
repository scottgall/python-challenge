import csv
from collections import defaultdict

with open('resources/election_data.csv', 'r') as csv_file:
  with open('analysis/election_results.txt', 'w') as new_file:
    csv_reader = csv.DictReader(csv_file)

    votes = 0

    candidates = defaultdict(int)

    for line in csv_reader:
      votes += 1
      candidates[line['Candidate']] += 1
    
    winner = max(candidates, key=lambda k: candidates[k])

    output = "Election Results\n"
    output += "------------------------\n"
    output += "Total Votes: {} \n".format(votes)
    output += "------------------------\n"
    for c,v in candidates.items():
      output += "{}: {:.3f}% ({})\n".format(c, (v/votes*100), v)
    output += "------------------------\n"
    output += "Winner: {}\n".format(winner)
    output += "------------------------\n"

    print(output)
    new_file.write(output)