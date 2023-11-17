import csv
import os

cvspath = os.path.join("..","Resources","budget_data.csv")

# Initialize variables
TotalMonths = 0
NetTotal = 0
LastProfit = 0
MonthlyChanges = []
Months = []

with open(cvspath, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    header = next(csv_reader)

    for row in csv_reader:
        # Date and Profit/Loss values
        date = row[0]
        profit = int(row[1])

        # Calculate the total months and net total Profit/Loss
        TotalMonths += 1
        NetTotal += profit

        # Calculate the monthly changes in Profit/Loss
        if TotalMonths > 1:
            change = profit - LastProfit
            MonthlyChanges.append(change)
            Months.append(date)

        LastProfit = profit

# Calculate the avg monthly change
AvgChange = round(sum(MonthlyChanges) / len(MonthlyChanges), 2)

# Find the greatest increase and decrease in Profit
max_increase = max(MonthlyChanges)
max_decrease = min(MonthlyChanges)
max_increase_month = Months[MonthlyChanges.index(max_increase)]
max_decrease_month = Months[MonthlyChanges.index(max_decrease)]

# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetTotal}")
print(f"Average Change: ${AvgChange}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Export the result
output_file = "financial_analysis.txt"
with open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {TotalMonths}\n")
    output.write(f"Total: ${NetTotal}\n")
    output.write(f"Average Change: ${AvgChange}\n")
    output.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    output.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")
