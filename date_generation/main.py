import argparse
import datetime 
from dateutil.relativedelta import relativedelta

def main(month,period,year):
    print("===========Start running date_generation.py===========")
    # make sure the arguments are valid
    month = int(month)
    period = int(period)
    year = int(year)
    assert (1 <= month) and (month <= 12), "Please make sure your starting month is between 1 and 12"
    assert year >= 1, "Please ensure that your year is positive (BC is not supported yet unfortunately)!"
    assert period >= 1, "Please ensure that your period is positive"

    # define dictionaries
    dic_month = {1: "January",
                 2: "February",
                 3: "March",
                 4: "April",
                 5: "May",
                 6: "June",
                 7: "July",
                 8: "August",
                 9: "September",
                 10: "October",
                 11: "November",
                 12: "December"}
    dic_week = {1: "M",
                2: "Tu",
                3: "W",
                4: "Th",
                5: "F",
                6: "Sa",
                0: "Su"}

    # Processing data
    print("Processing data to be saved in the txt")
    L = []
    start_date = datetime.date(year, month, 1)
    end_date = start_date + relativedelta(months =+ period)
    print("Your starting date will be", str(start_date), 
          ", and your ending date will be", str(end_date))
    current_date = start_date
    while current_date < end_date:
        day_of_week = int(current_date.strftime('%w'))
        current_month = int(current_date.month)
        current_day = int(current_date.day)
        if period < 12:
            result = dic_month[current_month] + " " + str(current_day) + " " + dic_week[day_of_week]
        else:
            current_year = int(current_date.year)
            result = dic_month[current_month] + " " + str(current_day) + " " + str(current_year) + " " + dic_week[day_of_week]
        L.append(result)
        current_date = current_date + relativedelta(days=+ 1)
    
    # write to a txt file
    print("Saving the results to a txt file")
    file_name = "date_for_" + str(period) + "_months.txt"
    f = open(file_name,"w")
    for each in L:
        f.write(each + "\n" + "\n")
    f.close()

    print("The txt file is saved!")
    print("===========End of date_generation.py===========")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description = 'Generate the date and day of the week string for a given period')
    parser.add_argument("-p", "--period", default=4,
                        help="An positive interger for the number of month needed. Default is 4 months")
    parser.add_argument("-y", "--year",
                        help="An positive interger for the year of the starting month")
    parser.add_argument("-m","--month",
                        help="The starting month that is an interger between 1 and 12")
    args = parser.parse_args()
    main(args.month, args.period,args.year)
