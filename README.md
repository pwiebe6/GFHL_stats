# GFHL_stats 
Useful for scraping all player data for a fantasy hockey season on ESPN. 
Two methods exist:
 1. Selenium based website scraping
    - Pros:
      - data is stored in easy to read csv files
    - Cons:
      - requires system with python/selenium/gui(?) in order to scrape data 
 2. Curl based scraping to json:
    - Pros:
      - Any machine can scrape the data
    - Cons:
      - json is a less human readable (not too much of a problem)

# Future Plans
1. Continue work with the website html. Looks like you can display the data from json files. Since there is more data in the json files than the csv files you will probably prioritize that going forward.
   - Next steps are to have the javascript in the dailies.html file automatically size the table headers based on the contents of the json
     - This idea is being scrapped. There's no reason to have this done dynamically for now. MUCH easier to manually define the columns and it's not difficult to update if required
   - Try to integrate dropdown menus to select different years and dates
     - First iteration in place. Could use some cleanup, but it is functional. Would like to add "prev-day" and "next-day" buttons for ease of use.
   - Integreate filters to hide/show columns. Default should look similar to the layout in the app, but users should be able to add/remove colums
     - This idea is being scrapped. There's no reason to have this done dynamically for now. MUCH easier to manually define the columns and it's not difficult to update if required
   - contunue effort to display skater stats on the dailies page. Most of it is hard coded for goalies so you'll need to do some massaging
     - once skaters are displayed reasonably well, fix the skipAppend implementation. Would like to skip if skaters GP=0. Unsure exactly how to implement for goalies but it might just be OR'ing all their stats to see if they played.
   - integrate options to show 25/50/100/all rows (maybe)
   - Continue effort with styling each page (low priority)

3. Utilize the fact the scraping script can work with different days to scrape previous days data. This will allow late data to trickle in.
   - currently only grabs yesterdays data early in the AM, but easily expandable to any date

5. Create script to convert json to csv so a more visible set of data can be left in the repo. (maybe not required if I can create a webpage that takes in json instead of csv as it will have more data)
   - This may be skipped in favour of converting CSV to JSON since I have HTML/JS to display JSON. Debating exactly what to do.

7. Cleanup script to convert csv to html and automatically add links (this path may be cut since json seems like it has a viable path forward)
   - Still need to add links to the all the html pages
   - Need to update the names of some files to keep things cleaner. Eg. https://www.gfhl.ca/dailies/2024/skaters/Skaters-2023-12-29.html doesn't need "skaters/Skaters"
     - Remove the second "Skaters", or remove both "skaters" and merge the skater and goalie stats together
   - Need to cleanup the html output
     - no need for the numbers on the left
     - look into sortable/filterable tables?
   - Is this a good method? These HTML files are 5 times the size of the csv files they're made from. Can this be done in a more sensible way?
     - I believe the path forward is to convert csv to json. Then a single html document can access all the json data instead of requiring am html document for each date.

8. Add command line arguments to the selenium scraper for:
   - COMPLETE: Skaters/Goalies
   - COMPLETE: year
   - COMPLETE: date range
   - NHL team specific
   - GFHL team specific
   - Add better logging to script
