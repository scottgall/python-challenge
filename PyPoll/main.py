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
    new_file.write(output)