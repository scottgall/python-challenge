# python-challenge

This is a repo for 2 Python challenges, `PyBank` & `PyPoll`. The `main.py` file in each directory contains a script that reads in data from a `.csv` file and outputs analysis to the `terminal` and a `.txt` file.

## PyBank

[PyBank/main.py](PyBank/main.py) reads through the financial records of a company in [budget_data.csv](PyBank/resources/budget_data.csv) and calculates the following:

* Total number of months included in the dataset
* Net total amount of "Profit/Losses"
* Average of the changes in "Profit/Losses"
* Greatest increase in profits (date & amount)
* Greatest decrease in losses (date & amount)

The financial analysis resembles the snippet below:
```
Financial Analysis
------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
```

## PyPoll
[PyPoll/main.py](PyPoll/main.py) reads through a town's polling data in [election_data.csv](PyPoll/resources/election_data.csv) and calculates the following:

* Total number of votes cast
* List of candidates who received votes
  * Percentage of votes each candidate won
  * Total number of votes each candidate won
* Winner of the election based on popular vote

The election results resemble the snippet below:
```
Election Results
------------------------
Total Votes: 3521001 
------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
------------------------
Winner: Khan
------------------------
```