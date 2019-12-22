# 
import os
import csv

# Set initial values for calculations
total_months = 0
net_total = 0
profit_loss_change = 0
average_change = []
greatest_increase = []
greatest_decrease = []

# Define name for CSV file
csv_path = os.path.join('budget_data.csv')
with open(csv_path, newline="") as financial_records:
    csvreader = csv.reader(financial_records, delimiter=",")

    #
    csv_header = next(csvreader)

    for row in csvreader:
        # Tells me that "row" is the first column
        print(row)
        # Tells me that "row[1] is the second column"
        print(row[1])

        # Add to the total by an increment (+=) of 1
        total_months += 1
        net_total += int(row[1])

    #print(total_months)
    #print(net_total)

    # Cycle through profits/losses column to get the monthly change
    #for i in range(len(row[1])):
        
        # Take the difference between two months and append to monthly profit change
        #profit_loss_change = (net_total[i+1]-=net_total[i])



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
#print(f"Average Change: {}")
#print(f"Greatest Increase in Profits: {}")
#print(f"Greatest Decrease in Profits: {}")

        




