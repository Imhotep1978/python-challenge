import os
import csv

# create path to csv file
file_path_input = os.path.join("Resources", "budget_data.csv")

# define the function
def budget_info(monthly_info):

    # # set variables for min, max, sum, average
    # datadate = str(monthly_info[0])
    revenue = int(monthly_info[1])
    
    
with open(file_path_input) as csvfile:
    # read csv file
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    print(header)
    # set count of months to zero
    count = 0
    # set budget to zero
    sum_budget = 0
    # set the previous month to zero
    previous_month_budget = 0
    # list to store budget difference
    list_budget_diff = []

    for row in csvreader: 
        print(type(row[1]))
        revenue = int(row[1])
        count = count + 1
        sum_budget = sum_budget + revenue
        differ_budget = previous_month_budget - revenue
        list_budget_diff.append(differ_budget)
        previous_month_budget = revenue
        print(sum_budget)
        print(previous_month_budget)
        print(differ_budget)
       
        
print(f'There is a total of {count} months.')
print(f'Total budget:  ${sum_budget}')

average_diff = sum(list_budget_diff)/len(list_budget_diff)
print(f'The average change each month is ${average_diff}')

# output file path
results_txt = os.path.join("results")

# # open the output file and write the text to te folder
with open(results_txt, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([])
