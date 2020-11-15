import os
import csv

data= os.path.join("./Resources/PyPoll_election.csv")

with open(data) as csvfile:
    election_data= csv.reader(csvfile, delimiter=',')
    csv_header= next(election_data)

    total_votes= 0
    candidates= []

    for row in election_data:
        total_votes += 1
        candidates.append(row[2])

    # Calculating the total number of votes each candidate won
    Khan_votes= candidates.count('Khan')
    Correy_votes= candidates.count('Correy')
    Li_votes= candidates.count('Li')
    oTooley_votes= candidates.count("O'Tooley")

    #Calculating the percentage of votes each candidate won
    total_votes += 1
    Khan_percent= (int(Khan_votes)/int(total_votes)) * 100
    Correy_percent= (int(Correy_votes)/int(total_votes)) * 100
    Li_percent= (int(Li_votes)/int(total_votes)) * 100
    oTooley_percent= (int(oTooley_votes)/int(total_votes)) * 100

    #Output
    print(f"Election Results")
    print(f"------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------")
    print(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
    print(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
    print(f"Li: {Li_percent:.3f}% ({Li_votes})")
    print(f"O'Tooley: {oTooley_percent:.3f}% ({oTooley_votes})")
    print(f"------------------------")

    output_file= os.path.join("./Analysis/Election_results.txt")
    with open(output_file, "w") as file:
        file.write(f"Election Results")
        file.write(f"------------------------")
        file.write(f"Total Votes: {total_votes}")
        file.write(f"------------------------")
        file.write(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
        file.write(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
        file.write(f"Li: {Li_percent:.3f}% ({Li_votes})")
        file.write(f"O'Tooley: {oTooley_percent:.3f}% ({oTooley_votes})")
        file.write(f"------------------------")



 
