# GFHL_stats
Useful for scraping all player data for a fantasy hockey season on ESPN.
Two methods exist:
 1. Selenium based website scraping
    - Pros:
      - data is stored in easy to read csv files
    - Cons:
      - requires system with python/selenium/gui(?)/ESPN tokens in order to scrape data 
 3. Curl based scraping to json:
    - Pros:
      - Any machine can scrape the data
    - Cons:
      - json is a less than ideal format
      - currently commits daily data overtop of yesterdays results - still need to clean up and save as easier to access files (csv)

# Future Plans
1. Continue work with the website html. Looks like you can display the data from json files. Since there is more data in the json files than the csv files you will probably prioritize that going forward.
   - Next steps are to have the javascript in the dailies.html file automatically size the table headers based on the contents of the json
     - I hope each entry has the same keys, or this will be very difficult...
   - need to fix the sorting algorithm. Currently sorts alphabet correctly, but numbers are sorted "alphabetically" too. ie. 0 -> 10 -> 2 -> 3
   - Try to integrate dropdown menus to select different years and dates
   - Integreate filters to hide/show columns. Default should look similar to the layout in the app, but users should be able to add/remove colums
   - integrate options to show 25/50/100/all rows (maybe)
   - Continue effort with styling each page

3. Utilize the fact the scraping script can work with different days to scrape previous days data. This will allow late data to trickle in.

4. Create script to convert json to csv so a more visible set of data can be left in the repo. (maybe not required if I can create a webpage that takes in json instead of csv as it will have more data)

5. Cleanup script to convert csv to html and automatically add links (this path may be cut since json seems like it has a viable path forward)
   - Still need to add links to the all the html pages
   - Need to update the names of some files to keep things cleaner. Eg. https://www.gfhl.ca/dailies/2024/skaters/Skaters-2023-12-29.html doesn't need "skaters/Skaters"
     - Remove the second "Skaters", or remove both "skaters" and merge the skater and goalie stats together
   - Need to cleanup the html output
     - no need for the numbers on the left
     - look into sortable/filterable tables?
   - Is this a good method? These HTML files are 5 times the size of the csv files they're made from. Can this be done in a more sensible way?

6. Add command line arguments to the selenium scraper for:
   - COMPLETE: Skaters/Goalies
   - COMPLETE: year
   - COMPLETE: date range
   - NHL team specific
   - GFHL team specific
   - Add better logging to script
