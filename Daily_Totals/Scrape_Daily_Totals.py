# Selenium Test 1

import time
import math
import numpy as np
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import colorama
from colorama import Fore
from colorama import Style
import traceback
import datetime
#from datetime import datetime
#from datetime import timedelta
import argparse

stub = True
stub_variable = 0

############################ EDIT ME #############################
# just to prevent from going all the way to the end for now
#MAX_PAGE = 10

# Add my teams name to show in blue
my_team = "CLB"
# Add opponent name to show opposing players in yellow
opponent = "BBS"
# skip showing opposing players in yellow
# opponent = "NULL"

# Show Free Agents in Green
free_agents = "FA"
# skip showing opponents in Green
# free_agents = "NULL"

#position = "S" # "S" for Skater or "G" for Goalies

#starting_year = "2023"  # Only 2021 is selectable for now. Need to implement scraping from other years

#scoringPeriodIdMin = 1
#scoringPeriodIdMax = 179 # 201 or maybe 203

############################# END EDIT ME ##################################

# create dictionary with season and starting dates
starting_dates = {
    #       [First Date on stats page | Start date  | End date    |scoring period Max]
    2019 : ["Wednesday, October 3",   "2018-10-03", "2019-04-06", 186],
    2020 : ["Wednesday, October 2",   "2019-10-02", "2020-06-21", 264], #Shortened year
    2021 : ["Wednesday, January 13",  "2021-01-13", "2021-05-19", 110], #Shortened year
    2022 : ["Tuesday, October 12",    "2021-10-12", "2022-04-29", 200],
    2023 : ["Tuesday, October 7",     "2022-10-07", "2023-04-02", 178],
    2024 : ["Tuesday, October 10",    "2023-10-10", "2024-04-04", 179],
    2025 : ["Friday, October 4",      "2024-10-04", "2025-04-17", 195],
    2026 : ["Tuesday, October 7",     "2025-10-07", "2025-04-16", 191]
}

GFHL_teams = ["FA", "DINK", "BOWS", "LKR", "OXP", "NBUS", "CLB", "HERB", "SALT", "ME", "BBS", "SLC", "HYD"]

# Webpage of today's top 50 skater by fpoints earned
#daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311"
#daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod&scoringPeriodId=29"

# https://fantasy.espn.com/hockey/leaders?leagueId=59311&seasonId=2019&statSplit=singleScoringPeriod&scoringPeriodId=1
#url = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod"
# leagueId = 59311
# seasonId = 2019
# statSplit = singleScoringPeriod
# scoringPeriodId = 1
# For Goalie stats
# lineupSlot = 5




#Set up colour class
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def TODO(message):
    '''Prints a string to the console with a "TODO:" prefix'''
    print("TODO: " + message)

def setup():
    '''Does setup.
    Returns browser driver.'''
    # Locate the Chrome drive used to launch the web scraper
    service = Service(r'C:\Users\pcw12\Downloads\Selenium\chromedriver-win32\chromedriver-win32\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    time.sleep(3)
    return(Chrome(options=options, service=service))

def scrape_page(driver, isGoalie):
    '''Scrapes the current page. Returns List of Lists'''
    # Grab all the tbody elements named "Table__TBODY". First three entries within that list are:
    # 1. player names (+teams, position, owner, opponent, game score),
    # 2. stat breakdown (GP, G, A, etc), and
    # 3. fantasy points.
    tbody = driver.find_elements(By.CLASS_NAME, "Table__TBODY")
    
    # Split up names, stats, and fantasy points
    names = tbody[0].text # 7
    stats = tbody[1].text # 16 for players, 6 for goalies
    fpts  = tbody[2].text # 1

    if(isGoalie):
        num_stats = 6
    else:
        num_stats = 16

    names = names.split("\n")
    names_list = []
    temp_list = []

    i = 0
    for name in names:
        # if the game opponent column indicates '--', add  '--' for the gametime/score
        if ((i%7 - 4) == 0):
            if ((name not in GFHL_teams)):
                temp_list.append('--')
                #
                i = i + 1

        # if there is no mention of 'DTD'/'IR'/'O'/'SSPD' in the health column, add 'Healthy'
        if ((i%7 - 1) == 0):
            if ((name != 'DTD') and (name != 'IR') and (name != 'O') and (name != 'SSPD')):
                temp_list.append('Healthy')
                #
                i = i + 1

        # if the game opponent column indicates '--', add  '--' for the gametime/score
        if ((i%7 - 5) == 0):
            if ((name == '--')):
                temp_list.append('--')
                #
                i = i + 1

        temp_list.append(name)
        i = i + 1
        if (i%7 == 0):
            #push append the temp_list to the names_list and clear the temp list
            names_list.append(temp_list)
            temp_list = []

    #print("PRINTING NAMES LIST" + str(names_list))

    stats = stats.split("\n")
    stats_list = []
    temp_list = []

    i = 0
    for stat in stats:
        if stat == '--':
            temp_list.append(stat)
        else:
            temp_list.append(int(stat))
        i = i + 1
        if (i%num_stats == 0):
            #push appended the temp_list to the stat_list and clear the temp list
            stats_list.append(temp_list)
            temp_list = []

    #print("PRINTING STATS LIST" + str(stats_list))

    fpts = fpts.split("\n")
    fpts_list = []
    temp_list = []

    for fpt in fpts:
        if fpt == '--':
            temp_list.append(fpt)
        else:
            temp_list.append(float(fpt))

        #push appended the temp_list to the stat_list and clear the temp list
        fpts_list.append(temp_list)
        temp_list = []

    #print("PRINTING FPTS LIST" + str(fpts_list))

    combined = []
    print("PRINTPRINTPRINT")
    print(len(names_list))
    print(len(stats_list))
    print(len(fpts_list))
    for i in range(len(names_list)):
        #print(names_list[i] + stats_list[i] + fpts_list[i])
        combined.append(names_list[i] + stats_list[i] + fpts_list[i])             
    return(combined)

def get_page_number(driver):
    '''Looks for the highlighted page number and returns the value of the current page (int)'''
    page = driver.find_element(By.XPATH, "//li[@class='Pagination__list__item pointer inline-flex justify-center items-center Pagination__list__item--active']")
    return(int(page.text))

def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.XPATH, "//button[@class='Button Button--default Button--icon-noLabel Pagination__Button Pagination__Button--next']")
        next_button.click()
    except:
        return("Unable to click. Perhaps the element does not exist on this page")

def go_to_prev_page(driver):
    try:
        next_button = driver.find_element(By.XPATH, "//button[@class='Button Button--default Button--disabled Button--icon-noLabel Pagination__Button Pagination__Button--previous Button--disabled']")
        next_button.click()
    except:
        return("Unable to click. Perhaps the element does not exist on this page")

def go_to_page(page):
    ''' Don't think this can work. Unable to select every single page by number'''
    if stub:
        print("go_to_page stub")
    else:
        print("go_to_page function not written yet")

def date_to_scoring_period(date):
    year = int(date[0:4])
    month = int(date[5:7])
    if (month >=10):
        year = year + 1
    return(year, days_between(starting_dates[year][1], date)+1)

def days_between(d1, d2):
    date_format = "%Y-%m-%d"
    a = datetime.datetime.strptime(d1, date_format)
    b = datetime.datetime.strptime(d2, date_format)
    delta = b - a
    return(delta.days)

def scoring_period_to_date(year, scoringPeriodId):
    days_offset = scoringPeriodId - 1

    date_string = starting_dates[year][1]
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    new_date = date + datetime.timedelta(days=days_offset)
    format_code = "%Y-%m-%d"
    return(new_date.strftime(format_code))

def get_date():
    if stub:
        print("get_date stub")
        return("Monday, November 8")
    else:
        print("get_date function not written yet")

def go_to_date():
    if stub:
        print("go_to_date stub")
    else:
        print("go_to_date function not written yet")

def check_if_played_today(item):
    '''ALWAYS RETURNS TRUE FOR NOW. Will be fixed when historical data doesn't get messed up by trades'''
    return(True)
    if(item[5] == '--'):
        return(False)
    else:
        return(True)

def round_nearest(x, a):
    '''Round x to the nearest a'''
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

def calculate_fpts(item, position):
    '''Used to double check ESPN's numbers'''
    if(position == "G"):
        num_stats = 6
    else:
        num_stats = 16


    sum = 0
    for i in range(0, num_stats):
        # Fix any missing stats to zero
        if item[i+7] == '--':
            item[i+7] = 0
        sum += scoring[i] * int(item[i+7])
    return(round_nearest(sum, 0.05))
    
def log_discrepancy(string):
    '''Right now print discrepancy message to screen. One day write to a log file'''
    print(Fore.RED + "DISCREPANCY: " + str(string) + Style.RESET_ALL)

def add_to_database(name, date):
    if stub:
        print("add_to_database stub")
    else:
        print("add_to_database function not written yet")

def check_database(name, date):
    if stub:
        print("check_databade stub")
    else:
        print("check_databade function not written yet")

def printFA(item):
    '''Print in Green if player is a Free Agent'''
    #print(item[4])
    if item[4] == free_agents:
        print(Fore.GREEN + str(item) + Style.RESET_ALL)
    elif item[4] == my_team:
        print(Fore.CYAN + str(item) + Style.RESET_ALL)
    elif item[4] == opponent:
        print(Fore.YELLOW + str(item) + Style.RESET_ALL)
    else: 
        print(item)

def writeFA(item, scoringId, fileName):
    #Write code to write item (list) as a csv
    # First clean the data by turning commas into something else
    for k in range(len(item)):
        item[k] = (str(item[k])).replace(",", "-")
    try:
        with open(fileName, "a") as file:
            file.write((str(item).replace("[", "").replace("]", "").replace("'", "")))
            file.write("\n")
    except Exception as e:
        traceback.print_exc()

def selectGoalies(driver):
    driver.find_elements(By.XPATH, '//label[@class="control control--radio picker-option"]')[4].click()
    wait_until_page_is_loaded(driver)
#    try:
#        buttons = []
#        for buttons in driver.find_elements(By.XPATH, '//label[@class="control control--radio picker-option"]'):
#            buttons.click()
#            wait_until_page_is_loaded(driver)
#            
#    except Exception as e:
#        traceback.print_exc()


def wait_until_page_is_loaded(driver):
    time.sleep(5)
    try:
        checkElement = expected_conditions.presence_of_element_located(By.XPATH, "//li[@class='Pagination__list__item pointer inline-flex justify-center items-center Pagination__list__item--active']")
        WebDriverWait(driver, 3).until(checkElement)      
    except:
        pass


def main():
    parser = argparse.ArgumentParser(
                    prog='Scrape_Daily_Totals.py',
                    description='Scrapes Daily totals from ESPN Fantasy hockey team',
                    epilog='Text at the bottom of help')
    
    parser.add_argument('-v', '--verbose', action='count', default=0, help="Used for debug prints at the moment")
    parser.add_argument('-r', '--run', action='store_true', default=False, help="Used for testing purposes. Required to scrape.")
    parser.add_argument('-s', '--startdate', default='NULL', help="Enter YYYY-MM-DD to manually select date. Defaults to today.")
    parser.add_argument('-e', '--enddate', default='NULL', help="Enter YYYY-MM-DD to manually select last date of range. Defaults to today.")
    parser.add_argument('-b', '--blueteam', default="NULL", help="Select team to highlight in blue")
    parser.add_argument('-y', '--yellowteam', default="NULL", help="Select team to highlight in yellow")
    parser.add_argument('-g', '--greenteam', default="FA", help="Select team to highlight in green")
    parser.add_argument('-G', '--goalie', action='store_true', default=False, help="Used to scrape Goalie stats instead of Skater stats.")
    parser.add_argument('-Y', '--year', type=int, default=2019, help="Provide the year that the season started in if using scoringId")
    parser.add_argument('-S', '--startscoringperiod', type=int, default=0, help="Provide starting scoring period. Must also provide Year with -Y")
    parser.add_argument('-E', '--endscoringperiod', type=int, default=0, help="Provide ending scoring period. Must also provide Year with -Y")
    parser.add_argument('-N', '--numdates', type=int, default=1, help="Provide number of dates to check. Default is 1")
    parser.add_argument('-M', '--maxpage', type=int, default=3, help="Provide number of pages to scrape per day. Default 5")
    parser.add_argument('-F', '--force_url', default="NULL", help="Provide a URL to start scraping from")


    args = parser.parse_args()

    # Do some checks here
    # For example the args.year variable shouldn't be less than 2019
    # If endscoringid is zero, to startscoringid + 1 to just capture at startscoringid
    if args.startdate != "NULL":
        year, scoringPeriodIdStart = date_to_scoring_period(args.startdate)
        if args.enddate != "NULL":
            null, temp = date_to_scoring_period(args.enddate)
            scoringPeriodIdEnd = temp + 1
        else:
            scoringPeriodIdEnd = scoringPeriodIdStart + args.numdates
    elif args.startscoringperiod != 0:
        year = args.year
        scoringPeriodIdStart = args.startscoringperiod
        if args.endscoringperiod != 0:
            scoringPeriodIdEnd = args.endscoringperiod
        else:
            scoringPeriodIdEnd = scoringPeriodIdStart + args.numdates
    # if no dates or scoringId is given then maybe just get today somehow
    else:
        year = args.year
        scoringPeriodIdStart = 1
        scoringPeriodIdEnd = 2


    if year < min(list(starting_dates.keys())):
        print("Year " + year + " invalid. Changing to" + min(list(starting_dates.keys())))
        year = min(list(starting_dates.keys()))

    url = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod"

    if args.goalie == 1:
        positionString = "5" # &lineupSlot=5 for goalies
        # scoring: GS, W,  L,   GA, SV, SO
        scoring = [ 0, 4, -1, -0.5, 0.1, 2]
        csvHeader = "Name, Health, NHL Team, Position, GFHL Team, Opponent, Score, GS, W, L, GA, SV, SO, FPTS"
        MAX_PAGE = 4
    else:
        positionString = "0%2C1%2C2%2C3%2C4%2C6" # &lineupSlot=0%2C1%2C2%2C3%2C4%2C6 for al skaters
        # scoring: GP, G, A,   +/-, PIM,  PPG, PPA,  SHG, SHA,  GWG, FOW, FOL,  HAT, SOG, HIT, BLK
        scoring = [ 0, 2, 1.5, 0.5, -0.1, 0.5, 0.25, 1  , 0.75, 1,   0.1, -0.1, 2,   0.1, 0.3, 0.5]
        csvHeader = "Name, Health, NHL Team, Position, GFHL Team, Opponent, Score, GP, G, A, +/-, PIM, PPG, PPA, SHG, SHA, GWG, FOW, FOL, HAT, SOG, HIT, BLK, FPTS"
        MAX_PAGE = 30

    if (args.verbose > -1):
        print("Run: " + str(args.run))
        print("Verbosity: " + str(args.verbose))
        print("Start Date: " + str(args.startdate))
        if args.startdate != "NULL":
            print("\tIn scoringId format: " +  str(date_to_scoring_period(args.startdate)))
        print("End Date: " + str(args.enddate))
        if args.enddate != "NULL":
            print("\tIn scoringId format: " +  str(date_to_scoring_period(args.enddate)))
        print("Blue Team: " + str(args.blueteam))
        print("Yellow Team: " + str(args.yellowteam))
        print("Green Team: " + str(args.greenteam))
        print("Goalie scraping? " + str(args.goalie))
        print("Year: " + str(year))
        print("Start Scoring Period: " + str(args.startscoringperiod))
        print("End Scoring Period: " + str(args.endscoringperiod))
        print("Number of dates: " + str(args.numdates))
        print("Max Page: " + str(args.maxpage))
        if args.force_url == "NULL":
            print("URL: " + str(url + "&scoringPeriodId=" + str(scoringPeriodIdStart) + "&seasonId=" + str(year) + "&lineupSlot=" + positionString))
        else:
            print("Forced URL: " + args.force_url)

    # Early exit for testing purposes
    if (args.run == False):
        return(False)
    else:
        pass


    colorama.init()
    # try to load today's top 50 skaters by fpoints earned
    try:
        driver = setup()

        for scoringPeriodId in range(scoringPeriodIdStart, scoringPeriodIdEnd):
            print("scoring Period = " + str(scoringPeriodId))
            # Open the browser
            driver.get(url + "&scoringPeriodId=" + str(scoringPeriodId) + "&seasonId=" + str(year) + "&lineupSlot=" + positionString)

            # Wait for page to load 
#            time.sleep(3)
#            TODO("Replace with better method of waiting for page load")
            wait_until_page_is_loaded(driver)

#            time.sleep(1)

            if (args.goalie == 1):
#                selectGoalies(driver)
                fileName = "temp//Goalies-" + str(scoring_period_to_date(year, scoringPeriodId)) + ".csv"
            else:
                fileName = "temp//Skaters-" + str(scoring_period_to_date(year, scoringPeriodId)) + ".csv"

            try:
                with open(fileName, "a") as file:
                    file.write(csvHeader)
                    file.write("\n")
            except Exception as e:
                traceback.print_exc()

            # Wait for page to load 
            TODO("Replace with better method of waiting for page load")

            # Get page number
            current_page = get_page_number(driver)
            print("Start of Page: "+ str(current_page))

            # Define stop_scrape to False so that every player is scraped
            stop_scrape = False
            # Get all stats for all playing players
            print("MAX_PAGE: " + str(min(MAX_PAGE,args.maxpage)+1))
            for i in range(1, min(MAX_PAGE,args.maxpage)+1):
                # Get all stats for page
                stats_list = scrape_page(driver, args.goalie)
                # Iterate through list from page
                for item in stats_list:
                    # If the player has played today, print the stats. Otherwise, stop scraping.
                    if check_if_played_today(item):
                        # if the calculated fpts does not match the value given by ESPN print discrepancy, and correct the error
                        #calculated = calculate_fpts(item, position)
                        #if (calculated != item[-1]) and (item[-1] != '--'):
                        #    log_discrepancy(str(item) + " != " + str(calculated))
                        #    item[-1] = calculated
                        printFA(item)
                        writeFA(item, scoringPeriodId, fileName)
                    
                    # THIS DOES NOT WORK! Look at page 10 of https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod&scoringPeriodId=29
                    # Kyle Clifford was traded from STL to TOR and as a result he appears on the list hierarchechaly where he should; however, he does not have a game 
                    # tied to him (since toronto did not play that day). As a result the scraping ends early. We can keep this in for scraping totals right after a
                    # day is over, but for historical checking this WILL NOT work.
                    else:
                        # We're done collecting useful data at this point. continue to exit out of item loop
                        stop_scrape = True
                        break

                current_page = get_page_number(driver)
                print("End of Page: "+ str(current_page))
                if stop_scrape == True:
                    break
                
                # If we are not on the final page
                if ((i+1) < min(MAX_PAGE, args.maxpage)+1):
                    go_to_next_page(driver)
                    wait_until_page_is_loaded(driver)
                    # Get updated page number and print the start of page message
                    current_page = get_page_number(driver)
                    print("Start of Page: "+ str(current_page))
                    # If our current page does not line up with the page of the next loop, print error message
                    if (current_page != i+1):
                        print("ERROR: Somehow ended up on the wrong page. Saw: '" + str(get_page_number(driver)) + "' Expected: '" + str(i+1) + "'")

            TODO("Look at re-organizing algorithm in order to work with traded players. Find the 'THIS DOES NOT WORK' comment")

    except Exception as e:
        print("Exception: ")
        traceback.print_exc()
    finally:
        #close the browser when done, or upon error
        try:
            driver.quit()
        except:
            print("Error quitting driver. Perhaps it was not declared, or perhaps the Chrome web_driver needs an update?")
            # If chrome and the chrome web_driver are not on the same version it will cause an exception when trying to quit the driver.
            # Check chrome version with menu -> help -> about chrome and then go to:
            # https://chromedriver.chromium.org/downloads to check if there is a matching web_driver




if __name__ == "__main__":
    main()
