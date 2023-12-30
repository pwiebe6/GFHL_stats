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

stub = True
stub_variable = 0


# just to prevent from going all the way to the end for now
#MAX_PAGE = 10

# Add opponent n
# ame to show opposing players in yellow
opponent = "ME"
# skip showing opposing players in yellow
opponent = "NULL"

# create dictionary with season and starting dates
starting_dates = {
    #        [First Date on stats page | Start date  | End date    ]
    "2020" : ["Wednesday, January 13",  "2021-01-13", "2021-05-19"],
    "2021" : ["Tuesday, October 12",    "2021-10-12", "2022-04-29"],
    "2022" : ["Tuesday, October 12",    "2022-10-07", "2023-04-02"]
}

# Webpage of today's top 50 skater by fpoints earned
#daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311"
#daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod&scoringPeriodId=29"

position = "G" # "S" for Skater or "G" for Goalies

starting_year = "2022"  # Only 2021 is selectable for now. Need to implement scraping from other years

if (position == "G"):
    daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod&lineupSlot=5&scoringPeriodId="
    # scoring: GS, W,  L,   GA, SV, SO
    scoring = [ 0, 4, -1, -0.5, 0.1, 2]
    csvHeader = "Name, Health, NHL Team, Position, GFHL Team, Opponent, Score, GS, W, L, GA, SV, SO, FPTS"
    MAX_PAGE = 5

else:
    daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=singleScoringPeriod&scoringPeriodId="
    # scoring: GP, G, A,   +/-, PIM,  PPG, PPA,  SHG, SHA,  GWG, FOW, FOL,  HAT, SOG, HIT, BLK
    scoring = [ 0, 2, 1.5, 0.5, -0.1, 0.5, 0.25, 1  , 0.75, 1,   0.1, -0.1, 2,   0.1, 0.3, 0.5]
    csvHeader = "Name, Health, NHL Team, Position, GFHL Team, Opponent, Score, GP, G, A, +/-, PIM, PPG, PPA, SHG, SHA, GWG, FOW, FOL, HAT, SOG, HIT, BLK, FPTS"
    MAX_PAGE = 29

scoringPeriodIdMin = 1
scoringPeriodIdMax = 179 # 201 or maybe 203

#  force for now
daily_leader = "https://fantasy.espn.com/hockey/leaders?leagueId=59311&statSplit=currSeason&scoringPeriodId=0"
scoringPeriodIdMin = 1
scoringPeriodIdMax = 2
MAX_PAGE = 5

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
    service = Service(r'C:\Users\pcw12\Downloads\Selenium\chromedriver_win32\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    time.sleep(3)
    return(Chrome(options=options, service=service))

def scrape_page(driver, position):
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

    if(position == "G"):
        num_stats = 6
    else:
        num_stats = 16

    names = names.split("\n")
    names_list = []
    temp_list = []

    i = 0
    for name in names:
        # if there is no mention of 'DTD'/'IR'/'O'/'SSPD' in the health column, add 'Healthy'
        if ((i%5 - 1) == 0):
            if ((name != 'DTD') and (name != 'IR') and (name != 'O') and (name != 'SSPD')):
                temp_list.append('Healthy')
                #
                i = i + 1


        temp_list.append(name)
        i = i + 1
        if (i%5 == 0):
            #push append the temp_list to the names_list and clear the temp list
            names_list.append(temp_list)
            temp_list = []

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

    combined = []
    print("PRINTPRINTPRINT")
    print(len(names_list))
    print(len(stats_list))
    print(len(fpts_list))
    for i in range(len(names_list)):
        print(names_list[i] + stats_list[i] + fpts_list[i])
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

def date_to_scoring_period():
    print("temp")

def scoring_period_to_date(scoringPeriodId):
    days_offset = scoringPeriodId - 1

    date_string = starting_dates[starting_year][1]
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
    if item[4] == 'FA':
        print(Fore.GREEN + str(item) + Style.RESET_ALL)
    elif item[4] == "CLB":
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
    time.sleep(1)
    try:
        checkElement = expected_conditions.presence_of_element_located(By.XPATH, "//li[@class='Pagination__list__item pointer inline-flex justify-center items-center Pagination__list__item--active']")
        WebDriverWait(driver, 3).until(checkElement)      
    except:
        pass


def main():
    colorama.init()
    # try to load today's top 50 skaters by fpoints earned
    try:
        driver = setup()

        for scoringPeriodId in range(scoringPeriodIdMin, scoringPeriodIdMax):
            # Open the browser
            driver.get(daily_leader) # + str(scoringPeriodId))

            # Wait for page to load 
#            time.sleep(3)
#            TODO("Replace with better method of waiting for page load")
            wait_until_page_is_loaded(driver)

            time.sleep(60)

            if (position == "G"):
#                selectGoalies(driver)
                fileName = "temp//Goalies-" + str(scoring_period_to_date(scoringPeriodId)) + ".csv"
            else:
                fileName = "temp//Skaters-" + str(scoring_period_to_date(scoringPeriodId)) + ".csv"

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
            print("MAX_PAGE: " + str(MAX_PAGE))
            for i in range(1, MAX_PAGE):
                # Get all stats for page
                list = scrape_page(driver, position)
                # Iterate through list from page
                for item in list:
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

                # Go to next page
                go_to_next_page(driver)
                wait_until_page_is_loaded(driver)

                
                # If we are not on the final page
                if (i+1) != MAX_PAGE:
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