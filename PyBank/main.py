import  os
import csv

# Define PyBank's variables
mon = []
pnl_changes = []

mon_count = 0
net_pnl = 0
prev_mon_pnl = 0
curr_mon_pnl = 0
pnl_change = 0


# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csvheader = next(csvfile)

             
    # Read through each row of data after the header
    for row in csvreader:

        # Count of months
        mon_count += 1

        # Net total amount of pnl over the entire period
        curr_mon_pnl = int(row[1])
        net_pnl += curr_mon_pnl

        if (mon_count == 1):
            # Make the value of previous month to be equal to current month
            prev_mon_pnl = curr_mon_pnl
            continue

        else:

            # Compute change in profit loss 
            pnl_change = curr_mon_pnl - prev_mon_pnl

            # Append each month to the mon[]
            mon.append(row[0])

            # Append each pnl_change to the pnl_changes[]
            pnl_changes.append(pnl_change)

            # Make the cur_month_loss to be prev_mon_pnl for the next loop
            prev_mon_pnl = curr_mon_pnl

    # Sum and Average of the changes in pnl over the entire period
    sum_pnl = sum(pnl_changes)
    average_pnl = round(sum_pnl/(mon_count - 1), 2)

    # Highest and Lowest changes in pnl over the entire period
    highest_change = max(pnl_changes)
    lowest_change = min(pnl_changes)

    # Locate the index value of highest and lowest changes in pnl over the entire period
    highest_month_index = pnl_changes.index(highest_change)
    lowest_month_index = pnl_changes.index(lowest_change)

    # Assign the best and worst month
    best_month = mon[highest_month_index]
    worst_month = mon[lowest_month_index]

# -->>  Print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {mon_count}")
print(f"Total: ${net_pnl}")
print(f"Average Change: ${average_pnl}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})")


# -->>  Export text file with results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {mon_count}\n")
    outfile.write(f"Total: ${net_pnl}\n")
    outfile.write(f"Average Change:  ${average_pnl}\n")
    outfile.write(f"Greatest Increase in Profits: {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses: {worst_month} (${lowest_change})\n")