# Import modules
import os
import csv

# Writing path to read csv file
csv_path = os.path.join("..", "python-challenge", "PyBank", "Resources", "budget_data.csv")
print(csv_path)
# Opening csv file to read
with open(csv_path) as csv_budget:
    csv_reader = csv.reader(csv_budget, delimiter= ",")
    
    # Skips header in csv file
    csv_header = next(csv_reader)
    
    # Creating counters to track data in csv file
    counter = 0
    total_prof = 0

    # Dictionaries to replace with desired values from data in csv file
    greatest_dict = {
        "date" : "",
        "profit" : 0
    }
    least_dict = {
        "date" : "",
        "loss" : 0
    }

    # Scans each row in csv file
    for row in csv_reader:
        
        # Counts all rows, in this case it will give the total months in data set as well
        counter = counter + 1

        # Adding up all integers in column 2 
        total_prof = total_prof + int(row[1])
        
        # Updating dictionaries previously set with desired data
        if int(row[1]) > greatest_dict["profit"]:
            greatest_dict.update ({"date": row[0], "profit": int(row[1])})
        
        if int(row[1]) < least_dict["loss"]:
            least_dict.update ({"date": row[0], "loss": int(row[1])})

    # Show Results in Terminal        
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", counter)

    # Utilization of f-strings to achieve correct formatting when printing
    print(f'Total: ${total_prof}')
    print(f'Average Change: ${"%.2f" % (total_prof/counter)}')
    print(f'Greatest Increase in Profits:, {greatest_dict["date"]} (${greatest_dict["profit"]})')
    print(f'Greatest Decrease in Profits:, {least_dict["date"]} (${least_dict["loss"]})')

    # Creating new file txt file in Analysis folder, "w" sets the script to overwrite file when ran
    clean_data_file = open(os.path.join("", "Analysis", "Financial_Analysis.txt"), "w")

    # Copied over print data from above to be written into txt file, swapping to f-strings simplified process when having to include /n to bring data to a new line
    clean_data_file.write(f'Financial Analysis\n')
    clean_data_file.write(f'----------------------------\n')
    clean_data_file.write(f'Total Months: {counter}\n')
    clean_data_file.write(f'Total: ${total_prof}\n')
    clean_data_file.write(f'Average Change: ${"%.2f" % (total_prof/counter)}\n')
    clean_data_file.write(f'Greatest Increase in Profits:, {greatest_dict["date"]} (${greatest_dict["profit"]})\n')
    clean_data_file.write(f'Greatest Decrease in Profits:, {least_dict["date"]} (${least_dict["loss"]})\n')
