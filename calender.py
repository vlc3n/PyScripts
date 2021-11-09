import datetime
import calendar

def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


print("Please Insert your Datetime in this format: 01 01 2000")
date = input("Type in your Datetime: ")
print(findDay(date))


#Python Program to get a specific day from a datetime