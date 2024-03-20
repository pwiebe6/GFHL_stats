import pandas as pd
from pathlib import Path
import os

#Very slow way of updating all docs/dailies/*.html files from the /Daily_Totals/Dailies/*.csv files

current_path = Path.cwd()  # Get the current working directory as a Path object
parent_path = current_path.parent
dailies_path = parent_path / "Daily_totals/Dailies"
html_path = parent_path / "docs/dailies"


print(f"Parent directory (using pathlib): {parent_path}")

if not os.path.exists(dailies_path):
    print(f"Error: The specified directory '{dailies_path}' does not exist.")
    exit
if not os.path.exists(html_path):
    print(f"Error: The specified directory '{dailies_path}' does not exist.")
    exit

sep = os.path.sep

for subdir, dirs, files in os.walk(dailies_path):
    print("SUBDIR: " + str(subdir))
    for file in files:
        filename = os.path.join(subdir, file)
        print("FILENAME: " + str(filename))
        partial_path = filename.split(sep)[-3:]
        partial_path = partial_path[0] + sep + partial_path[1].lower() + sep + partial_path[2]
        partial_path = partial_path.replace(".csv", ".html")
        print("partial path: " + str(partial_path))



        destpath = html_path / partial_path
        print(destpath)
        
        # Read the CSV file
        stats = pd.read_csv(filename)
        
        # Convert to HTML and save to a file
        stats.to_html(destpath)

