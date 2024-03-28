import os
import glob
import csv

from pathlib import Path

NUM_SIZE = 10

def get_last_number_from_csv(csvfilename):
    last_numbers = []

    with open(csvfilename, 'r', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Avoid blank lines
                last_number = float(row[-1])  # Assuming the last value is numeric
                last_numbers.append(last_number)

    return last_numbers

current_path = Path.cwd()  # Get the current working directory as a Path object
parent_path = current_path.parent
dailies_path = parent_path / "Daily_totals/Dailies"

print(f"Parent directory (using pathlib): {parent_path}")

current_max = [ [ 0 for y in range( 3 ) ] for x in range( NUM_SIZE ) ]

# Validate if the directory exists
if not os.path.exists(dailies_path):
    print(f"Error: The specified directory '{dailies_path}' does not exist.")
else:
    for subdir, dirs, files in os.walk(dailies_path):
        for file in files:
         filename = os.path.join(subdir, file)

         with open(filename, 'r', encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # Avoid blank lines
                  if (row[-1] == " FPTS" or row[-1] == " --"):
                      continue
                  last_number = float(row[-1])  # Assuming the last value is numeric
                  if last_number >= current_max[0][0]:
                      print("file: " + filename + " Stat: " + str(row))
                      current_max[0][0] = last_number
                      current_max[0][1] = filename
                      current_max[0][2] = str(row)
                      current_max.sort()

    for i in range(len(current_max)):
        print(NUM_SIZE-i, ": \n\t", str(current_max[i][1][-14:-5]), "\n\t", str(current_max[i][2]))                  
