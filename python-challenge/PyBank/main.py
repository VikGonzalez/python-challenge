import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    change=[]
    change2=[]
    date=[]

    next(csvreader)
    months = 0
    amount = 0

    for row in csvreader:
        months = months+1
        amount = amount + float(row[1])
        z = float(row[1])
        change.append(z)
        x= str(row[0])
        date.append(x)

    for counter in range (months-1):
        y= change[counter+1]-change[counter]
        change2.append(y)
        avg = sum(change2)/len(change2)
        b= max(change2)
        c = date[counter+1]
        d= min(change2)
        e = date[counter+1]

    print("Financial Analysis")
    print ("--------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: {amount}")
    print(f"Average Change: {avg}")
    print(f"Greatest Increase in Profits: {c} {b} ")
    print(f"Greatest Increase in Profits: {e} {d} ")
