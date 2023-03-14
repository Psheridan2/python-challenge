# Importing modules
import os
import csv

# Writing path to read csv file
csv_path = os.path.join("..","python-challenge", "PyPoll", "Resources", "election_data.csv")
print(os.path.abspath(csv_path))

# Opening csv file to read
with open(csv_path) as csv_election:
    csv_reader = csv.reader(csv_election, delimiter= ",")

    # Skips header in csv file
    csv_header = next(csv_reader)

    # Creating counter to track data in csv file
    counter = 0

    # Creating dictionary to store values for candidate name and total votes
    candidates_dict = {

    }

     # Scans each row in csv file
    for row in csv_reader:

        # Counts all rows, in this case it will give the total # of votes in data set as well
        counter = counter + 1
        name = row[2]
        
        # Made to set keys for the below dictionary: Candidate Name, Value
        if name in candidates_dict.keys(): 
            candidates_dict[name] = candidates_dict[name] + 1
        else:
            candidates_dict[name] = 1

    # Printing into terminal
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {counter}')
    print(f'-------------------------')

    # Creating txt file to write data into
    clean_data_file = open(os.path.join("", "Analysis", "Election_Results.txt"), "w")
    
    # Writing Data into txt file
    clean_data_file.write(f'Election Results\n')
    clean_data_file.write(f'-------------------------\n')
    clean_data_file.write(f'Total Votes: {counter}\n')
    clean_data_file.write(f'-------------------------\n')

    # Creating Dictionary to store data of candidate with most votes
    winner_dict = {
        "name" : "",
        "votes" : 0
    }

    # Defining keys and creating new percentage value for each candidate
    for cand_name, vote_tally in candidates_dict.items():
        vote_percent = f'{"%.3f" % ((vote_tally/counter) * 100)}%'
        
        # Storing candidate with most votes into Winner Dictionary
        if vote_tally > winner_dict["votes"]:
            winner_dict["votes"] = vote_tally
            winner_dict["name"] = cand_name
        
        # Vote tally was breaking on the print, this fixed it
        vote_tally = f'({vote_tally})'
        
        print(cand_name, vote_percent, vote_tally)
        clean_data_file.write(f'{cand_name, vote_percent, vote_tally}\n')
    

    print(f'-------------------------')             
    print(f'Winner: {winner_dict["name"]}')
    print(f'-------------------------')
    

    
    clean_data_file.write(f'-------------------------\n')             
    clean_data_file.write(f'Winner: {winner_dict["name"]}\n')
    clean_data_file.write(f'-------------------------\n')

