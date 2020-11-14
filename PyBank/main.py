import os
import csv

data= os.path.join("./Resources/PyBank_budget.csv")

with open(data) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)


    total_months= 0
    profit_losses= []
    PandL_dates = []
    total_PL = 0
    max_pl = 0
    min_pl = 0
    total_PL_avg= 0

    for row in csvreader:
        total_months += 1
        profit_losses.append(int(row[1]))
        total_PL += int(row[1])
        PandL_dates.append(row[0])

    profitloss_change = []
    for i in range(1, len(profit_losses)):
        #calculating the difference between two consecutive rows
        change = profit_losses[i] - profit_losses[i - 1]
        profitloss_change.append(int(change))

    for i in range(0, len(profitloss_change)):
        total_PL_avg += profitloss_change[i]
        average_change_profitloss = round((total_PL_avg)/ (len(profitloss_change)), 2)
    
    for profloss in profit_losses:
        if min_pl == 0:
            max_pl == profloss
            min_pl == profloss
        if profloss > max_pl:
            max_pl = profloss
        elif profloss < min_pl:
            min_pl = profloss

    max_pl_index = profit_losses.index(max_pl)
    min_pl_index = profit_losses.index(min_pl)
    max_pl_date = PandL_dates[max_pl_index]
    min_pl_date = PandL_dates[min_pl_index]

    
    print (f"Financial Analysis") 
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_PL}")
    print(f"Average Change: ${average_change_profitloss}")
    print(f"Greatest Increase in Profits: {max_pl_date} (${max_pl}")
    print(f"Greatest Decrease in Profits: {min_pl_date} (${min_pl}")
    
    output_path = os.path.join("./Analysis/financial_analysis.txt")
    with open(output_path, 'w') as file:
        file.write(f"Financial Analysis")
        file.write(f"----------------------------")
        file.write(f"Total Months: {total_months}")
        file.write(f"Total: ${total_PL}")
        file.write(f"Average Change: ${average_change_profitloss}")
        file.write(f"Greatest Increase in Profits: {max_pl_date} (${max_pl})")
        file.write(f"Greatest Decrease in Profits: {min_pl_date} (${min_pl}")


