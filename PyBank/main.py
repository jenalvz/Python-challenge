#import libraries and dependencies
import os
import csv

#set the path for the csv file
file_budget = "Resources/budget_data.csv"

#declare variables to store data
total_profit = 0
total_month = 0
pre_profit = 0
change = 0
total_change = 0
month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""


#open the file and begin reading the data
with open(file_budget) as input_file:
    content = csv.reader(input_file)
    next(content)

    for row in content:

        total_profit = total_profit + int(row[1])
        total_month = total_month + 1
        
        current_profit = int(row[1])

        if pre_profit != 0:
            change = current_profit - pre_profit
            total_change = total_change + change
            month_change = month_change + 1

        pre_profit = current_profit

        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]


        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]

    avg_change = total_change/month_change


#print your new variable results in the terminal to ensure accuracy, then comment out so they wont interfere with the code
# print(avg_change)

# print(total_profit)
# print(total_month)
# print(greatest_increase)
# print(greatest_decrease)


#write output formula with verified variable results
output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: ${avg_change:,.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

print(output)

#create a separate text file with the final results
with open("Analysis/pybank_output.txt", "w") as txt_file:
    txt_file.write(output)
