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
1. Utilize the fact the scraping script can work with different days to scrape previous days data. This will allow late data to trickle in.

2. Create script to convert json to csv so a more visible set of data can be left in the repo.

3. Cleanup script to convert csv to html and automatically add links
   - Still need to add links to the all the html pages
   - Need to update the names of some files to keep things cleaner. Eg. https://www.gfhl.ca/dailies/2024/skaters/Skaters-2023-12-29.html doesn't need "skaters/Skaters"
     - Remove the second "Skaters", or remove both "skaters" and merge the skater and goalie stats together
   - Need to cleanup the html output
     - no need for the numbers on the left
     - look into sortable/filterable tables?
   - Is this a good method? These HTML files are 5 times the size of the csv files they're made from. Can this be done in a more sensible way?

4. Add command line arguments to the selenium scraper for:
   - COMPLETE: Skaters/Goalies
   - COMPLETE: year
   - COMPLETE: date range
   - NHL team specific
   - GFHL team specific
   - Add better logging to script
