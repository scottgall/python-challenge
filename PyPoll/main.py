import csv

with open('resources/election_data.csv', 'r') as csv_file:
  with open('analysis/election_results.txt', 'w') as new_file:
    csv_reader = csv.DictReader(csv_file)

    votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    cand = 'Candidate'

    for line in csv_reader:
      votes += 1
      if line[cand] == 'Khan':
        khan += 1
      elif line[cand] == 'Correy':
        correy += 1
      elif line[cand] == 'Li':
        li += 1
      elif line[cand] == "O'Tooley":
        otooley += 1

    candidates = {khan: "Khan", correy: "Correy", li: "Li", otooley: "O'Tooley"}
    winner = candidates.get(max(candidates))
      
    output = ("Election Results\n"
              "------------------------\n"
              "Total Votes: " + str(votes) + "\n"
              "------------------------\n"
              "Khan: " + str('{:.3f}%'.format(round(khan/votes*100, 3))) + " (" + str(khan) + ")\n"
              "Correy: " + str('{:.3f}%'.format(round(correy/votes*100, 3))) + " (" + str(correy) + ")\n"
              "Li: " + str('{:.3f}%'.format(round(li/votes*100, 3))) + " (" + str(li) + ")\n"
              "O'Tooley: " + str('{:.3f}%'.format(round(otooley/votes*100, 3))) + " (" + str(otooley) + ")\n"
              "------------------------\n"
              "Winner: " + str(winner) + "\n"
              "------------------------\n"
              )
    print(output)
    new_file.write(output)