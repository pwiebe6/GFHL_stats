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
Utilize the fact the scraping script can work with different days to scrape previous days data. This will allow late data to trickle in.

Create script to convert json to csv so a more visible set of data can be left in the repo.

Add script to convert csv to html and automatically add 

Add command line arguments for:
 -Skaters/Goalies
 -year
 -date range
 -NHL team specific
 -GFHL team specific

 Add better logging to script
