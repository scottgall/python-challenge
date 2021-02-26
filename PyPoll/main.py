import os
import csv
from collections import defaultdict

csv_file = os.path.join('resources', 'election_data.csv')
data_output = os.path.join('analysis', 'election_results.txt')

with open(csv_file) as csvfile:
  with open(data_output, 'w') as newfile:
    csv_reader = csv.DictReader(csvfile)

    votes = 0

    candidates = defaultdict(int)

    for line in csv_reader:
      votes += 1
      candidates[line['Candidate']] += 1
    
    winner = max(candidates, key=lambda k: candidates[k])

    output = f"Election Results\n" \
             f"------------------------\n" \
             f"Total Votes: {votes} \n" \
             f"------------------------\n"
    for c,v in candidates.items():
      output += f"{c}: {v/votes*100:.3f}% ({v})\n"
    output += f"------------------------\n" \
              f"Winner: {winner}\n" \
              f"------------------------\n"

    print(output)
    newfile.write(output)