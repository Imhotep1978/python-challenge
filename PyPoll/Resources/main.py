import csv
import os

# create a path to csv file
py_rollfile = os.path.join('Resources','election_data.csv')

#list to store data
Candidates = []

# read the CSV
with open(py_rollfile) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #header
    header = next(csvreader)

    #Add candidates
    Candidates = 0
    

print("The number of votes are: {total_votes}")

# output fle path
results_txt = os.path.join("results")

#open the output file and write the text to the folder
with open(results_txt, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([])