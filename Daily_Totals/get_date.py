# Getdate test

import time
import math
import traceback
import datetime


# create dictionary with season and starting dates
starting_dates = {
    #       [First Date on stats page | Start date  | End date    |scoring period Max]
    2019 : ["Wednesday, October 3",   "2018-10-03", "2019-04-06", 186],
    2020 : ["Wednesday, October 2",   "2019-10-02", "2020-06-21", 264], #Shortened year
    2021 : ["Wednesday, January 13",  "2021-01-13", "2021-05-19", 110], #Shortened year
    2022 : ["Tuesday, October 12",    "2021-10-12", "2022-04-29", 200],
    2023 : ["Tuesday, October 7",     "2022-10-07", "2023-04-02", 178],
    2024 : ["Tuesday, October 10",    "2023-10-10", "2024-04-04", 179]
}

def date_to_year(date):
    year = int(date[0:4])
    month = int(date[5:7])
    if (month >=10):
        year = year + 1
    print(year)
    return(year)

def date_to_scoringId(date):
    year = int(date[0:4])
    month = int(date[5:7])
    if (month >=10):
        year = year + 1
    print(days_between(starting_dates[year][1], date))
    return(days_between(starting_dates[year][1], date))

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
 



def main():
    print("main")



if __name__ == "__main__":
    main()
