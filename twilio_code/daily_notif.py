import time
from datetime import date
from twilio_code.HolidayAssign import HolidayAssign

def daily():
  # Dictionary of Dates to Holidays
    holidayList = HolidayAssign()
    date_holiday_dict = holidayList.create_dict()

    for holiday in date_holiday_dict.keys():
        holidays = date_holiday_dict.keys()

        if holidays[holiday.sub(0, holiday.find(" "))] == date.today.month & holidays[holiday.sub(holiday.find(" ") + 1), len(holiday)] == date.today.day:
            print("Today is: " + holidays[holiday])
            time.sleep(10)

if __name__ == "__main__":
    daily()