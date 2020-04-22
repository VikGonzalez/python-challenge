import os
import csv 

csvpath = os.path.join("Resources","PyPoll_election_data.csv")


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =",")
    print(next(csvreader))

    TotalK = 0
    TotalC = 0
    TotalL = 0
    TotalO = 0
    
    for row in csvreader:
        ElectionList =str(row[2])
        if ElectionList=="Khan":
             TotalK +=1
        elif ElectionList=="Correy":
             TotalC +=1    
        elif ElectionList=="Li":
             TotalL +=1
        elif ElectionList=="O'Tooley":
             TotalO +=1

        TotalVotes = TotalK + TotalC + TotalL + TotalO

        PercentVotesK=TotalK / TotalVotes
        PercentVotesC=TotalC / TotalVotes
        PercentVotesL=TotalL / TotalVotes
        PercentVotesO=TotalO / TotalVotes
       
    print("Election Results")
    print("----------------")
    print(f"Total Votes: {TotalVotes}")
    print("----------------")
    print(f"Total Votes Khan: {PercentVotesK:{1}.{4}}" + "%" + " " + "(" + str(TotalK)+ ")")
    print(f"Total Votes Correy: {PercentVotesC:{1}.{4}}"  + "%"+ " " + "(" + str(TotalC)+ ")")
    print(f"Total Votes Li: {PercentVotesL:{1}.{4}}" + "%"+ " " + "(" + str(TotalL)+ ")")
    print(f"Total Votes O'Toley: {PercentVotesO:{1}.{4}}"  + "%"+ " " + "(" + str(TotalO)+ ")")
    print("----------------")
    Winner = [TotalK, TotalC, TotalL, TotalO]
   
if TotalK == max(Winner):
     print("Winner: Khan")
elif TotalC == max(Winner):
     print ("Winner: Cole")
elif TotalL == max(Winner):
     print ("Winner Li")
elif TotalO== max(Winner):
     print ("Winner O´Toole")
               

    
