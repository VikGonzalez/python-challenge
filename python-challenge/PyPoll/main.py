import os #habilitar herramientas
import csv #importar módulo de CSV

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =",")

    next(csvreader)

    Total = len(list(csvreader))

    TotalK = 0
    TotalC = 0
    TotalL = 0
    TotalT = 0

    ElectionList = []
    for row in csvreader:
        ElectionList.append(str(row[2]))
        if ElectionList == "Khan":
            TotalK +=1
        elif ElectionList == "Correy":
            TotalC +=1    
        elif ElectionList == "Lee":
            TotalK +=1
        elif ElectionList == "Tooley":
            TotalT +=1 

            print("Election Results")
            print("----------------")
            print(f"Total Votes:    {Total}")
            print("----------------")
            print(f"Total Votes Khan: {TotalK}" + "(%)")
            print(f"Total Votes Khan: {TotalC}" + "(%)")
            print(f"Total Votes Khan: {TotalL}" + "(%)")
            print(f"Total Votes Khan: {TotalT}" + "(%)")
            print("----------------")


   


   